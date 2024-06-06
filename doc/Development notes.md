# Development Notes

## Fuente de datos
Dado que la API de Twitter no está abierta, la captura de datos se realizará desde un archivo a un topic de Kafka.

Para ello, he explorado los datasets de Twitter dentro de Kaggle y he elegido este:
https://www.kaggle.com/datasets/kazanova/sentiment140

Lo he ubicado en la carpeta [dataset](../dataset/).

## Conectar archivo con un topic de Kafka utilizando un source connector

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

O a la web de Control Center:
http://localhost:9021/clusters

Consumimos los mensajes del topic `tweets-input`:
```bash
kafka-console-consumer --bootstrap-server broker:9092 --topic tweets-input --from-beginning
```

## Crear el contenedor con el analizador de sentimientos

Especificaciones:
- El contenedor debe consumir del topic de kafka `tweets-input`
- Debe analizar los sentimientos de los tweets uno a uno - real time.
- Envía el resultado al topic de kafka `analyzed-tweets`

### Pruebas desde consola

Para correr el archivo desde consola, con el entorno de `predictor-env`:
```bash
conda env --list
conda activate predictor-env
python ./analyzer/app.py
```

Para copiar más archivos dentro del contenedor y comprobar que sigue consumiendo:
```bash
docker cp ./connectors/plaintext/dataset/twitter-extract-02.csv connect:/tmp/input/twitter-extract-02.csv
docker cp ./connectors/plaintext/dataset/twitter-extract-03.csv connect:/tmp/input/twitter-extract-03.csv
```

### Pruebas con el contenedor

Primero tengo que testear que el contenedor funciona:

```bash
cd analyzer
docker build -t sentiment_analyzer:v1 .

docker run -it sentiment_analyzer:v1
```

Después integraremos en el docker-compose.yml.