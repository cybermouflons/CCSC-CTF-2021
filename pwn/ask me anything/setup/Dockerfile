FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y socat gcc-multilib

# transfer files
WORKDIR /root
COPY pwn ./pwn
COPY flag.txt ./flag.txt
RUN chmod +x ./pwn

EXPOSE 51337
CMD ["socat", "-T60", "TCP-LISTEN:51337,reuseaddr,fork,su=root", "EXEC:/root/pwn"]
