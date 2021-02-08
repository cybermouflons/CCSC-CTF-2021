FROM python:3.8.1-slim

RUN apt-get update
RUN apt-get install -y socat gcc-multilib
RUN apt-get install -y less

# transfer files
WORKDIR /root
COPY chessportal.py ./chessportal.py
COPY flag.txt ./flag.txt

EXPOSE 4337
CMD ["socat", "-T60", "TCP-LISTEN:1991,reuseaddr,fork,su=root", "EXEC:'python3 -u chessportal.py'"]
