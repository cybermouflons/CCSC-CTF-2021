#!/bin/bash
# --security-opt=seccomp:unconfined
docker run -p 51337:51337 -d --restart=always ccsc2021/askmeanything
