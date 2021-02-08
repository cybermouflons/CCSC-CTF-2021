FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat gcc-multilib

# user
RUN adduser --disabled-password --gecos '' elliot

# transfer files
WORKDIR /home/elliot

COPY pwn ./pwn
COPY flag.txt ./flag.txt

RUN chown root:root /home/elliot/flag.txt ./pwn
RUN chmod +s ./pwn
RUN chmod 400 /home/elliot/flag.txt

EXPOSE 3337
CMD ["socat", "TCP-LISTEN:3337,reuseaddr,fork,su=elliot", "EXEC:/home/elliot/pwn"]