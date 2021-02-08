
FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat gcc-multilib

# set workdir and transfer binary
WORKDIR /root
COPY pwn .
COPY flag.txt .
COPY libc.so.6 .
COPY ld-linux-x86-64.so.2 .

EXPOSE 1337
CMD ["socat", "-vv","TCP-LISTEN:1337,reuseaddr,fork,su=root", "EXEC:'/root/pwn'"]
