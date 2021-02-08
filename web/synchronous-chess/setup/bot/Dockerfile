FROM buildkite/puppeteer:v1.15.0

COPY run.sh /
COPY admin.js /
RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
