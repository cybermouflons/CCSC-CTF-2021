flag = "CCSC{8x8?_thats_Sup3r_c0nven1ent_dont_y0u_agr33?i_think_it_is__}"
assert len(flag) == 64


def char2fen(c):
    s = ''
    k = 0
    for i in range(8):
        if not c & 1:
            k += 1
        else:
            if (k):
                s = s + str(k)
            k = 0
            s = s + 'P'
        c >>= 1
    if (k):
        s = s + str(k)

    return s[::-1]


x = [char2fen(ord(f)) for f in flag]
t = ['/'.join(x[i:i+8]) for i in range(0, len(x), 8)]
print(t)
