FROM hyperreality/cryptohack:latest

COPY . /home/sage/chall/

WORKDIR /home/sage/chall/

RUN sudo chmod -R 777 /home/sage/chall/

USER sage

RUN sage generate_chall.sage

