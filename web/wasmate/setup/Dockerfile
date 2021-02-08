FROM emscripten/emsdk AS builder

COPY . /chall
WORKDIR /chall
RUN emcc ./lib/chesslib.c  -o ./lib/chesslib.js  -s EXPORTED_FUNCTIONS='["_check_mate", "_free", "_malloc"]' -s MODULARIZE=1 -s EXTRA_EXPORTED_RUNTIME_METHODS='["allocateUTF8"]'

FROM bitnami/node

COPY --from=builder /chall /root/chall

WORKDIR /root/chall

RUN [ -f flag.txt ] && mv flag.txt /root/flag.txt
RUN tar -cf ../wasmate.tar.gz --exclude='flag.txt' .
RUN npm install pm2 -g && npm install

ENV HOME /tmp
CMD ["pm2-docker","start","app.js"]