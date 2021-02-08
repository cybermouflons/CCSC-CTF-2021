#!/bin/bash
# --security-opt=seccomp:unconfined
docker run -p 1991:1991 -d --restart=always ccsc2021/chessportal
