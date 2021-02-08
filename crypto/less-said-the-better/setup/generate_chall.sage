import os
import random
import itertools

from Crypto.Util.number import bytes_to_long, long_to_bytes

def gen_kmany_zero_lsb(k, bits, power=0):
    n = 1;
    while n & (pow(2,k) - 1) != 0:
        while power == 0:
            power = int.from_bytes(os.urandom(1), byteorder="little")
        base = ceil(getrandbits(bits)^(1/power))
        n = base^power
    return n, base, power


def find_two_power(base):
    if all(p != 2 for p , e in factor(base)):
        raise ValueError("Couldn't find factor 2")
    
    return [e for p , e in factor(base) if p == 2][0]

def find_special_prime(p, t, m):
    prime_candidates = []
    ring = IntegerModRing(2^(find_two_power(a)*m))
    for lsb_bits in itertools.product(('0','1'), repeat=t-1):
        r = int("".join(lsb_bits) +"1", 2)
        prime = p + r
        if ring(r) == ring(prime) and is_prime(prime):
            prime_candidates.append((prime, r))
    return random.choice(prime_candidates)

valid_params = False
while not valid_params:
    print("[+] Generating params...")

    m = int.from_bytes(os.urandom(1), byteorder="little")

    p, a, _ = gen_kmany_zero_lsb(12, 1024, m)
    q, b, _ = gen_kmany_zero_lsb(12, 1024, m)

    prime_p ,rp = find_special_prime(p, 12, m)
    prime_q, rq = find_special_prime(q, 12, m)

    assert (prime_p == pow(a,m) + rp) and is_prime(prime_p)
    assert (prime_q == pow(b,m) + rq) and is_prime(prime_q)

    N = prime_p * prime_q;
    c  = round(pow(N, 1/2) - floor(pow(prime_p, 1/2)) * floor(pow(prime_q, 1/2)));
    valid_params = c < 2^112
    
    print("Attack possible {0} < 2^112: {1}".format(c, valid_params))
    

with open("flag.txt", "rb") as f:
    flag = f.read()

e = 65537
phi = (prime_p-1)*(prime_q-1)
d = inverse_mod(e, phi)
orig_pt = bytes_to_long(flag)

assert gcd(phi, e) == 1
assert orig_pt < N

ct = pow(orig_pt, e, N)
pt = pow(ct, d, N)

assert long_to_bytes(pt) == flag

public_handout = f"""e={e}
p * q=N={N}
m={m}

p = a**m + rp
q = b**m + rq

p & (2**12-1) = {rp}
q & (2**12-1) = {rq}

ct = {ct}
"""

with open("chall.txt", "w") as f:
    f.write(public_handout)
    
print("[+] Challenge params saved at chall.txt")