# Development Notes

## Fuente de datos
Dado que la API de Twitter no está abierta, la captura de datos se realizará desde un archivo a un topic de Kafka.

Para ello, he explorado los datasets de Twitter dentro de Kaggle y he elegido este:
https://www.kaggle.com/datasets/kazanova/sentiment140

Lo he ubicado en la carpeta [dataset](../dataset/).

## Conectar archivo con un topic de Kafka

https://docs.confluent.io/kafka-connectors/spooldir/current/connectors/csv_source_connector.html#spooldir-csv-source-connector

Crear la imagen del contenedor connect:
```bash
cd ./connectors
docker build -t my-kafka-connect:v1 .
cd ..
docker-compose up -d
```

Inspeccionar el topic `tweets-input` y ver el resultado:

Entramos al contenedor del broker:
```bash
docker exec -it broker /bin/bash
```

Consumimos los mensajes del topic `tweets-input`:
```bash
kafka-console-consumer --bootstrap-server broker:9092 --topic tweets-input --from-beginning
```