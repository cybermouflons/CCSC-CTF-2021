FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive

# update db
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y && apt-get upgrade -y

# install a text editor
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nano build-essential
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libcap2-bin

# SSH
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-server
RUN service ssh start

# install python3
RUN apt-get install -y python3 python3-pip python3-dev

# add a user
RUN mkdir -p /home/hax
RUN groupadd hax
RUN useradd -g hax -s /bin/bash hax
RUN chown -R hax:hax /home/hax/
RUN echo 'hax:hax' | chpasswd

# copy flag and change permissions to 400 (root:root)
COPY flag.txt /home/hax/flag.txt
RUN chown root:root /home/hax/flag.txt
RUN chmod 400 /home/hax/flag.txt

# set capability
RUN chown root:root /usr/bin/python3.8
RUN setcap "cap_sys_admin+eip" /usr/bin/python3.8

WORKDIR /home/hax/

# expose port
EXPOSE 6666

CMD ["/usr/sbin/sshd", "-D", "-p", "6666"]
