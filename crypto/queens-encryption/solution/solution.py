ct = '''
rnbk1bnr/p1pQpppp/1p1p4/8/3P4/2P5/PP2PPPP/RNB1KBNR
5k2/3Q2p1/p4n1r/1p3p2/1P4P1/1R2P3/P2KP1BP/2B4R
8/4k2r/p5p1/7n/1P2P1P1/1Q1R4/P3P1BP/2B1K2R
6k1/3Q4/8/p2n2p1/1P4P1/3RP2B/PB2P2R/3K4
3Q2k1/8/8/p3n1p1/1P4P1/2KR3B/PB2P2R/8
Q7/6k1/8/p3n3/1P4P1/2KR3B/PB2P2R/8
8/4kr1p/8/Q1P3P1/pp1r2p1/3B4/PP1K3P/3R1R2
r1bq2nr/pppkbppp/2n5/8/3P4/1Q6/PPP2PPP/RNB1KBNR
3q3r/5kbp/2b4n/p1rpp1p1/2P1PpPQ/PP1pnP1N/6BP/R1B1KN1R
3qr3/1p1bk1bp/r2p3n/p1p3p1/1nNPPp2/P1P2P1N/1P1Q2BP/R1B1K2R
3q3r/5kbp/1r2b2n/p1P3p1/P2pPBn1/1P1p1P1N/5QBP/2R1KN1R
2b2Q1r/7p/1R3n1b/3pkp2/2p3p1/r7/P1P2PPP/2B1KBR1
4k3/5r1p/8/ppPQ2P1/3r2p1/3B4/PP1K3P/3R1R2
5k1r/4n2p/8/8/8/8/P2Q3P/RNBK1BNR
4n1nB/p2rbk1p/8/8/7Q/8/PPKNR1PP/5BNR
r4b1r/ppnbnkpp/8/1Q6/8/8/PP4PP/RNB1KBNR
r3kbnr/p5pp/3Qb3/2p5/4p3/2P5/P5PP/R1B1KBNR
r1bqkbnr/pQ4pp/2n5/5pP1/8/2NPp3/PPP2P1P/R3KBNR
rnbqkbnr/pp4pp/2p5/3pppQ1/5P2/2PPP3/PP4PP/RNB1KBNR
'''.split('\n')

table = {
    'a1': ['09', '2d'],
    'a2': ['67', '5b'],
    'a3': ['05', '57'],
    'a4': ['34', '41'],
    'a5': ['31', '4f'],
    'a6': ['61', '66'],
    'a7': ['68', '08'],
    'a8': ['6e', '46'],
    'b1': ['14', '13'],
    'b2': ['51', '3b'],
    'b3': ['53', '52'],
    'b4': ['11', '25'],
    'b5': ['49', '36'],
    'b6': ['6d', '6f'],
    'b7': ['47', '7e'],
    'b8': ['4c', '0e'],
    'c1': ['10', '12'],
    'c2': ['6a', '29'],
    'c3': ['19', '3f'],
    'c4': ['6c', '42'],
    'c5': ['5c', '38'],
    'c6': ['0b', '69'],
    'c7': ['3c', '50'],
    'c8': ['71', '1d'],
    'd1': ['15', '73'],
    'd2': ['7a', '5f'],
    'd3': ['2c', '04'],
    'd4': ['44', '01'],
    'd5': ['65', '45'],
    'd6': ['2b', '4e'],
    'd7': ['2a', '43'],
    'd8': ['7b', '24'],
    'e1': ['37', '75'],
    'e2': ['26', '1c'],
    'e3': ['70', '03'],
    'e4': ['1b', '23'],
    'e5': ['18', '72'],
    'e6': ['35', '27'],
    'e7': ['0c', '22'],
    'e8': ['33', '74'],
    'f1': ['06', '7c'],
    'f2': ['54', '58'],
    'f3': ['1f', '7f'],
    'f4': ['30', '6b'],
    'f5': ['62', '3e'],
    'f6': ['4a', '2f'],
    'f7': ['00', '63'],
    'f8': ['48', '76'],
    'g1': ['78', '1a'],
    'g2': ['17', '55'],
    'g3': ['79', '21'],
    'g4': ['02', '0f'],
    'g5': ['77', '7d'],
    'g6': ['39', '1e'],
    'g7': ['16', '28'],
    'g8': ['5a', '07'],
    'h1': ['56', '0a'],
    'h2': ['59', '5e'],
    'h3': ['3d', '40'],
    'h4': ['32', '4b'],
    'h5': ['5d', '60'],
    'h6': ['4d', '3a'],
    'h7': ['20', '2e'],
    'h8': ['64', '0d'],
}

queen_positions = []
for c in ct:
    sc = c.split('/')
    for idx, rank in enumerate(sc):
        if 'Q' in rank:
            x = ord('a')
            y = 8 - idx
            for _, square in enumerate(rank):
                if square == 'Q':
                    break
                elif square.isdigit():
                    x += int(square)
                else:
                    x += 1
            queen_positions.append(f'{chr(x)}{y}')

print(queen_positions)


def bf(m, r):
    i = 0
    for i in range(1 << len(r)):
        s = ''
        for j, k in enumerate(r):
            if (1 << j & i):
                s += m[k][0]
            else:
                s += m[k][1]
        try:
            decoded = bytearray.fromhex(s).decode()
            if decoded.startswith('CCSC{') and decoded.endswith('}'):
                # The correct flag can be observed manually, but some "smart" heuristics can be
                # applied, based on the description, to reduce the noise.
                if any(x.lower() in decoded.lower() for x in ['pawn', 'bishop', 'knight', 'rook', 'queen', 'king']):
                    print(decoded)
        except:
            pass


bf(table, queen_positions)

# Flag: CCSC{FORK_THE_KING}
