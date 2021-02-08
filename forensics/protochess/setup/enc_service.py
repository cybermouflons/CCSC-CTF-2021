import grpc
import concurrent.futures

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
from os import environ

from enc_pb2 import AES_ECB, AES_CBC, AES_CTR, FlagResponse
from enc_pb2_grpc import add_EncryptServicer_to_server,EncryptServicer

PORT = '50051' or environ.get('ENC_PORT')

class AESCipher:
    def __init__(self, key, mode):
        if len(key) != 32:
            raise ValueError("Key must be of length 32")

        self.key = key if isinstance(key, bytes) else key.encode('utf-8')
        
        if mode == AES_ECB:
            self.mode = AES.MODE_ECB
        elif mode == AES_CBC:
            self.mode = AES.MODE_CBC
        elif mode == AES_CTR:
            self.mode = AES.MODE_CTR
        else:
            raise ValueError("Unsupported mode.")

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, self.mode, iv)
        return iv, self.cipher.encrypt(
            pad(data if isinstance(data, bytes) else data.encode('utf-8'), AES.block_size)
        )

    def decrypt(self, iv, data):
        self.cipher = AES.new(self.key, self.mode, iv)
        return unpad(self.cipher.decrypt(data), AES.block_size)

class EncryptService(
    EncryptServicer
):
    def encrypt(self, request, context):
        aes = AESCipher(key=request.key, mode=request.mode)
        flag = open("flag.txt","rb").read()
        iv, enc_flag = aes.encrypt(flag)
        return FlagResponse(iv=iv, flag=enc_flag)

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    add_EncryptServicer_to_server(
        EncryptService(), server
    )
    
    print(f"Serving at [::]:{PORT}")

    server.add_insecure_port(f"[::]:{PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()