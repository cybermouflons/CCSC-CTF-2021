FROM ubuntu:latest

# update db
RUN apt-get update -y

# add gcc
RUN apt-get install -y nano socat gcc build-essential

# add a user
RUN mkdir -p /home/hax
RUN groupadd hax
RUN useradd -g hax -s /bin/bash hax
RUN chown -R hax:hax /home/hax/

# copy flag and change permissions to 400 (root:root)
COPY flag.txt /home/hax/flag.txt
RUN chown root:root /home/hax/flag.txt
RUN chmod 400 /home/hax/flag.txt

# make ld.so.preload world-writable
RUN touch /etc/ld.so.preload
RUN chmod 666 /etc/ld.so.preload

RUN echo 'hax:hax' | chpasswd


# change to user hax0r
# USER hax
WORKDIR /home/hax/

ARG DEBIAN_FRONTEND=noninteractive
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y openssh-server

RUN service ssh start

# expose port
EXPOSE 6667

CMD ["/usr/sbin/sshd", "-D", "-p", "6667"]

# CMD ["/bin/bash"]
# CMD ["socat", "-v","TCP-LISTEN:6667,reuseaddr,fork,su=hax", "EXEC:'/bin/bash'"]
