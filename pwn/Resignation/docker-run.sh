#!/bin/bash
# --security-opt=seccomp:unconfined
docker run -p 4337:4337 -d --restart=always ccsc2021/resignation
