from Cryptodome.Random import get_random_bytes
from Cryptodome.Random.random import randint
from Cryptodome.Util.number import getPrime

class PRNG:
    
    def __init__(self):
        self.n = getPrime(8*8, randfunc=get_random_bytes)
        self.m = int.from_bytes(get_random_bytes(8), byteorder="big") % self.n
        self.c = int.from_bytes(get_random_bytes(8), byteorder="big") % self.n
        self.state = int.from_bytes(get_random_bytes(8), byteorder="big") % self.n
        for _ in range(randint(128, 1024)):
            self.state = self.next()
        
    def next(self):
        self.state = (self.state * self.m + self.c) % self.n
        return self.state
    
    def next_as_hex(self):
        return hex(self.next())[2:]