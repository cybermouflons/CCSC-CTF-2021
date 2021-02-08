FROM ubuntu

# update db
RUN apt-get update -y

# add python3
RUN apt-get install -y python3 libcap2-bin
RUN apt-get install -y apt-utils nano
RUN apt-get install -y build-essential gcc

# add a user
RUN mkdir -p /home/hax
RUN groupadd hax
RUN useradd -g hax -s /bin/bash hax
RUN chown -R hax:hax /home/hax/

# copy flag and change permissions to 600 (root:root)
COPY flag /home/hax/
RUN chown root:root /home/hax/flag
RUN chmod 400 /home/hax/flag

# c'mon
RUN touch /etc/ld.so.preload
RUN chmod 666 /etc/ld.so.preload

# Remove DIS
# COPY poc.c /home/hax/poc.c
# RUN gcc -shared -o /home/hax/libcustom.so -fPIC /home/hax/poc.c
# RUN chmod 777 /home/hax/poc.c

# change to user hax0r
USER hax
WORKDIR /home/hax/

CMD [ "/bin/bash" ]
