from Crypto.Util.number import long_to_bytes

with open("chall.txt", "r") as f:
    params = f.readlines()

for line in params:
    if line.startswith("e="):
       exec(line)
    elif line.startswith("p * q=N="):
        exec(line[6:])
    elif line.startswith("m="):
        exec(line)
    elif line.startswith("p & (2**12-1)"):
        rp = int(line[len("p & (2**12-1) = "):])
    elif line.startswith("q & (2**12-1)"):
        rq = int(line[len("q & (2**12-1) = "):])
    elif line.startswith("ct ="):
        exec(line)

lower_bound = ceil(pow(rp*rq, 1/2))
higher_bound = ceil((rq/2) + pow(2, m/2 - 1) * rp + 1)

for i in range(lower_bound, higher_bound):
    sigma = pow(floor(sqrt(N)) - i,2)
    z = Integer(IntegerModRing(sigma)(N - rp*rq))
    x_1, x_2 = solve(x^2 - z*x + sigma*rp*rq == 0,x)
    if (x_1.rhs() in ZZ): break

p = N / (x_1.rhs()/rq + rp)
q = N / (x_2.rhs()/rp + rq)

assert p*q == N

print("p: ", p)
print("q: ", q)

phi = (p-1)*(q-1)
d = inverse_mod(e, phi)
pt = pow(ct, d, N)

print("Flag: ", long_to_bytes(pt))
print("Attack completed!")