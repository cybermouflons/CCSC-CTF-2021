
# Curve Definition
# y**2 = x**3 + 255537741223171757577906131137465038503x + 235551977898890531700524068012369054363 mod 280394458065053566564172062910380346917
#
# G = (1, 108205897630675315269406380269889759312)
# P = d1*G = (200420486036538165442375859655970044012, 183075742307484235685368806654763094770)
# Q = d2*G = (35508838373018720116467153354135142477, 191774085631476756742536290957916295493)
# K = d1*d2*G = d2*P = d1*Q

from Crypto.Cipher import AES
from hashlib import sha256

aes = AES.new(sha256(K[0].to_bytes(16, 'big')).digest(), AES.MODE_ECB)
flag = open('flag.txt').read().strip()
cipher = aes.encrypt(flag.ljust((len(flag) + 15) // 16 * 16 ).encode());

with open("flag.enc","w") as f:
    f.write(cipher.hex())