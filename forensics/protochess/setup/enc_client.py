import grpc
import os

from os import environ

from enc_pb2 import EncryptRequest, AES_CBC
from enc_pb2_grpc import EncryptStub

HOST = environ.get('ENC_HOST', None) or 'localhost' 
PORT = environ.get('ENC_PORT', None) or '50051'

print(f"Connecting to {HOST}:{PORT}")
channel = grpc.insecure_channel(f"{HOST}:{PORT}")
client = EncryptStub(channel)

key = os.urandom(32)
request = EncryptRequest(key=key, mode=AES_CBC)

response = client.encrypt(request)

print(response)