#!/bin/bash
# --security-opt=seccomp:unconfined
docker run -p 41337:41337 -d --restart=always ccsc2021/chessanalyzer
