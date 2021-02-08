import os

base_dir = os.path.dirname(os.path.abspath(__file__))
borgovs_moves = "18. Bg5 Bxc4 19. dxc4 Qe6 20. Qd3 Rfd8 21. b3 Nh5 22. Be3 Nxg3 23. fxg3 h5 24. Qe2 Kg7"
flag = open(os.path.join(base_dir, "flag.txt"),"r").read()