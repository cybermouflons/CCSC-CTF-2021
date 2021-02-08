key = [0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74]
enc_str= [0x014,0x088,0x058,0x144,0x090,0x09c,0x14c,0x0c8,0x0b8,0x084,0x0ba,0x070,0x0a6,0x024,0x064,0x04a,0x04e,0x05a,0x070,0x01a,0x010,0x056,0x01b,0x035,0x021,0x03e,0x009,0x03d,0x021,0x026]

# shift right 2 bits 0-9
for i in range(10):
    enc_str[i] = enc_str[i]>>2

# shfit right 1 bit 10-19
for i in range(10,20):
    enc_str[i] = enc_str[i]>>1

# Xor with key
for i in range(len(enc_str)):
    enc_str[i]= enc_str[i] ^ key[i]

# Change positions
temp = enc_str[7]
enc_str[7]= enc_str[3]
enc_str[3]= enc_str[1]
enc_str[1]= temp

temp = enc_str[8]
enc_str[8] = enc_str[4]
enc_str[4] = enc_str[2]
enc_str[2] = temp

temp= enc_str[6]
enc_str[6] = enc_str[5]
enc_str[5] = temp

temp = enc_str[9]
enc_str[9] = enc_str[0]
enc_str[0] = temp

temp = enc_str[17]
enc_str[17]= enc_str[13]
enc_str[13]= enc_str[11]
enc_str[11]= temp

temp = enc_str[18]
enc_str[18] = enc_str[14]
enc_str[14] = enc_str[12]
enc_str[12] = temp

temp= enc_str[16]
enc_str[16] = enc_str[15]
enc_str[15] = temp

temp = enc_str[19]
enc_str[19] = enc_str[10]
enc_str[10] = temp

temp = enc_str[27]
enc_str[27]= enc_str[23]
enc_str[23]= enc_str[21]
enc_str[21]= temp

temp = enc_str[28]
enc_str[28] = enc_str[24]
enc_str[24] = enc_str[22]
enc_str[22] = temp

temp= enc_str[26]
enc_str[26] = enc_str[25]
enc_str[25] = temp

temp = enc_str[29]
enc_str[29] = enc_str[20]
enc_str[20] = temp

res = ""
for i in range(len(enc_str)):
    res += chr(enc_str[i])

print(res)
