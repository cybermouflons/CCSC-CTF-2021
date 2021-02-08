from parse import parse

with open("encrypt.py") as f:
    lines = f.readlines()
    
for line in lines:
    if line.startswith("# y**2 = x**3"):
        r = parse("# y**2 = x**3 + {A:d}x + {B:d} mod {p:d}\n", line)
        a, b, p = r['A'], r['B'], r['p']
    elif line.startswith("# G = "):
        r = parse("# G = ({G_x:d}, {G_y:d})\n", line)
        G = (r["G_x"], r["G_y"])
    elif line.startswith("# P = "):
        r = parse("# P = d1*G = ({P_x:d}, {P_y:d})\n", line)
        P = (r["P_x"], r["P_y"])
    elif line.startswith("# Q = "):
        r = parse("# Q = d2*G = ({Q_x:d}, {Q_y:d})\n", line)
        Q = (r["Q_x"], r["Q_y"])
    
set_verbose(-2)

print("p: ", p)
print("A: ", a)
print("B: ", b)

F = GF(p)
R.<k>=PolynomialRing(F)

A.<x,y>=F[]
C=Curve(x^3+a*x+b-y^2)

print("Curve: ", C)
assert C.is_singular()

R.<k> = PolynomialRing(F)
E = k^3 + a*k + b

S = C.singular_points()[0];
print("Singular Point at: ", S)

print("Translating curve....")

E_ = E.subs(k=k+S[0])
P_ = (P[0] - S[0], P[1])
Q_ = (Q[0] - S[0], Q[1])
G_ = (G[0] - S[0], G[1])

print(E_)
E_f =  E_.factor()

print(E_f)

assert (0, 0) == (0, E_(0))

t = E_f[0][0][0].square_root()
print("t^2 == {0}".format(E_f[0][0][0]))
print("t: ", t)

assert t in F

Fg = (G_[1] + t*G_[0]) / (G_[1] - t*G_[0]) % p
Fq = (Q_[1] + t*Q_[0]) / (Q_[1] - t*Q_[0]) % p
Fp = (P_[1] + t*P_[0]) / (P_[1] - t*P_[0]) % p

dl1 = Fp.log(Fg)
print("Discrete Log 1: ", dl1)

dl2 = Fq.log(Fg)
print("Discrete Log 2: ", dl2)

# Ref: Elliptic Curves: Number theory and Cryptography. Theorem 2.31 Page 62

Fk =  F ((Fg ^ dl1) ^ dl2)

Kx = F(4* (t^2) * Fk) / F((Fk - 1)^2)
Ky = F(4 * (t ^ 3) * Fk * (Fk + 1)) / F((Fk - 1)^3)
K = (Kx+S[0], Ky)

print("Recovered Secret: ", K)

from Crypto.Cipher import AES
from hashlib import sha256

aes = AES.new(sha256(int(K[0]).to_bytes(Integer(16), 'big')).digest(), AES.MODE_ECB)
flag_enc = bytes.fromhex(open('flag.enc').read().strip())
flag = aes.decrypt(flag_enc);

print(flag)
