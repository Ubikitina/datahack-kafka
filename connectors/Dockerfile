FROM confluentinc/cp-kafka-connect:7.2.2

RUN confluent-hub install --no-prompt jcustenborder/kafka-connect-spooldir:2.0.65

RUN mkdir /tmp/input && mkdir /tmp/finok && mkdir /tmp/finerr && exit

COPY ./plaintext/dataset/twitter-extract-01.csv /tmp/input/twitter-extract-01.csv

COPY ./plaintext/connect-file-source.json .

COPY start.sh .

CMD ["/bin/sh", "start.sh"]