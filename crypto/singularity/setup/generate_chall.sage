# from sage.misc.verbose import set_verbose

set_verbose(-2)

# https://crypto.stackexchange.com/questions/61302/how-to-solve-this-ecdlp
# https://ask.sagemath.org/question/48982/sagemath-refuses-to-load-singular-curve/
# https://martinlauridsen.info/pub/intro_to_pairings_lattices.pdf

def discriminant(a,b):
    return 4*a^3 + 27*b^2

def add_points(a1, a3, a2, a4, a6, p1, p2, K):
    if p1 == infinity:
        return p2
    elif p2 == infinity:
        return p1
    
    x1 = K(p1[0]); y1 = K(p1[1]); x2 = K(p2[0]); y2 = K(p2[1]);
    if x1 != x2:
        lamb = (y2 - y1)/(x2 - x1)
        mu = (y1*x2 - y2*x1)/(x2 - x1)
    else:
        if y1 == -y2:
            return infinity
        lamb = (3*x1^2 + 2*a2*x1 + a4 - a1*y1)/(2*y1 + a1*x1 + a3)
        mu = (-x1^3 + a4*x1 + 2*a6 - a3*y1)/(2*y1 + a1*x1 + a3)
    x3 = lamb^2 + a1*lamb - a2 - x1 - x2
    return (x3, -(lamb + a1)*x3 - mu - a3)

def point_scalar(a1, a3, a2, a4, a6, n, P, K):
# determine reverse binary expansion of n
    nb = [int(x) for x in bin(n)[2:]][::-1]
    R = infinity
    Q = P
    for i in range(len(nb)):
        if nb[i] == 1:
            R = add_points(a1, a3, a2, a4, a6, R, Q, K) 
    Q = add_points(a1, a3, a2, a4, a6, Q, Q, K) # 
    return R


params_found = False
while not params_found:
    try:
        det_sol = []
        while len(det_sol) == 0:
            p = next_prime(getrandbits(128))
            F = GF(p)
            R.<k>=PolynomialRing(F)
            a = randint(2, p-1)
            det_sol=(4*a^3+27*k^2).roots();

        b = F(det_sol[0][0])

        assert discriminant(a,b) == 0

        print("p: ", p)
        print("A: ", a)
        print("B: ", b)

        A.<x,y>=F[]
        C=Curve(x^3+a*x+b-y^2)

        print("Curve: ", C)
        assert C.is_singular()

        R.<k> = PolynomialRing(F)
        E = k^3 + a*k + b

        print("Factorized Curve: ", E.factor())

        G = (1, E(1).square_root())
        C(G[0], G[1])
        print("Generator: ", G)

        print("Finding random points on curve:")
        d1 = randint(2, p-1)
        P = point_scalar(0,0,0, a ,b, d1, G, F)
        C(P[0], P[1])

        d2 = randint(2, p-1)
        Q = point_scalar(0,0,0, a ,b, d2, G, F)
        C(Q[0], Q[1])

        print("P: ", P)
        print("Q: ", Q)
        print("d1: ", d1)
        print("d2: ", d2)
        print("")
        print("P = d1*G")
        print("Q = d2*G")

        Psecret = point_scalar(0,0,0, a ,b, d2, P, F)
        print("P: Secret: ", Psecret)
        Qsecret = point_scalar(0,0,0, a ,b, d1, Q, F)
        print("Q: Secret: ", Qsecret)

        assert Psecret == Qsecret

        K = (int(Psecret[0]), int(Psecret[1]))

        # Make sure there is solution

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

        params_found = True
        
        K = (int(Psecret[0]), int(Psecret[1]))
    except Exception as e:
        print("[+] Failed to generate params... See error below:")
        print(type(e))
        print("[+] Retrying...")

from Crypto.Cipher import AES
from hashlib import sha256

aes = AES.new(sha256(K[0].to_bytes(16, 'big')).digest(), AES.MODE_ECB)
flag = open('flag.txt').read().strip()
cipher = aes.encrypt(flag.ljust((len(flag) + 15) // 16 * 16 ).encode());

with open("flag.enc","w") as f:
    f.write(cipher.hex())


from jinja2 import Template

template = Template("""
# Curve Definition
# {{ curve }}
#
# G = {{ G }}
# P = d1*G = {{ P }}
# Q = d2*G = {{ Q }}
# K = d1*d2*G = d2*P = d1*Q

from Crypto.Cipher import AES
from hashlib import sha256

aes = AES.new(sha256(K[0].to_bytes(16, 'big')).digest(), AES.MODE_ECB)
flag = open('flag.txt').read().strip()
cipher = aes.encrypt(flag.ljust((len(flag) + 15) // 16 * 16 ).encode())

with open("flag.enc","w") as f:
    f.write(cipher.hex())
""")

output = template.render(
    curve=f"y**2 = x**3 + {a}x + {b} mod {p}",
    G=G,
    P=P,
    Q=Q,
)

with open("encrypt.py", "w") as f:
    f.write(output)