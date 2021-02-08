FROM ubuntu

# update db
RUN apt-get update -y

# add python3
RUN apt-get install -y python3 libcap2-bin

# install a text editor
RUN apt-get install -y apt-utils nano

# add a user
RUN mkdir -p /home/hax
RUN groupadd hax
RUN useradd -g hax -s /bin/bash hax
RUN chown -R hax:hax /home/hax/

# copy flag and change permissions to 600 (root:root)
COPY flag /home/hax/

# REMOVE DIS
# COPY exploit.py /home/hax/
# RUN chmod 777 /home/hax/exploit.py

RUN chown root:root /home/hax/flag
RUN chmod 400 /home/hax/flag

# set cap
RUN chown root:root /usr/bin/python3.8
RUN setcap "cap_sys_admin+eip" /usr/bin/python3.8

# change to user hax0r
USER hax
WORKDIR /home/hax/

CMD [ "/bin/bash" ]
