# Development Notes

## Fuente de datos
Dado que la API de Twitter no está abierta, la captura de datos se realizará desde un archivo a un topic de Kafka.

Para ello, he explorado los datasets de Twitter dentro de Kaggle y he elegido este:
https://www.kaggle.com/datasets/kazanova/sentiment140

Lo he ubicado en la carpeta [dataset](../dataset/).

## Conectar archivo con un topic de Kafka

https://docs.confluent.io/kafka-connectors/spooldir/current/connectors/csv_source_connector.html#spooldir-csv-source-connector

Entrar en el contenedor de `connect`:
```bash
docker exec -it connect bash
```

Instalar el Conector Spooldir Source Connector en el contenedor `connect`:
```bash
confluent-hub install --no-prompt jcustenborder/kafka-connect-spooldir:2.0.65
```

Crear carpetas y salir del contenedor:
```bash
mkdir /tmp/input && mkdir /tmp/finok && mkdir /tmp/finerr && exit
```

Para copiar el archivo a la ruta correcta dentro del contenedor de Connect, utilizamos el siguiente comando (ejecutado desde la carpeta del ejemplo):

```bash
docker cp ./dataset/training.10.processed.noemoticon.csv connect:/tmp/input/training.10.processed.noemoticon.csv
```

Reiniciar el contenedor connect y revisar los logs para esperar a que diga que está listo:
```bash
docker restart connect
docker logs -f connect
```

Iniciar un conector de texto plano con su configuración:

````sh
curl -d @"./kafka-connect/plaintext/connect-file-source.json" -H "Content-Type: application/json" -X POST http://localhost:8083/connectors
````

**Inspeccionar el topic `tweets-input` y ver el resultado**

Entramos al contenedor del broker:
```bash
docker exec -it broker /bin/bash
```

Consumimos los mensajes del topic `tweets-input`:
```bash
kafka-console-consumer --bootstrap-server broker:9092 --topic tweets-input --from-beginning
```