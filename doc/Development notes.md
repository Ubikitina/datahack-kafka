# Development Notes

## Otros importantes:
- Decir que tengo que hacer los builds de las imágenes antes.

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

Primero tenemos que crear el contenedor:

```bash
cd analyzer
docker build -t sentiment_analyzer:v1 .
```

Ahora lo probaremos habiendo integrado en el docker-compose.yml, consumiendo los mensajes del topic `analyzed-tweets`:
```bash
docker-compose up -d
docker exec -it broker /bin/bash

# Consumir en tweets-input
kafka-console-consumer --bootstrap-server broker:9092 --topic tweets-input --from-beginning

# Consumir en analyzed tweets
kafka-console-consumer --bootstrap-server broker:9092 --topic analyzed-tweets --from-beginning
```

Probamos que copiando más archivos dentro del contenedor y comprobar que sigue consumiendo:
```bash
docker cp ./connectors/plaintext/dataset/twitter-extract-02.csv connect:/tmp/input/twitter-extract-02.csv
docker cp ./connectors/plaintext/dataset/twitter-extract-03.csv connect:/tmp/input/twitter-extract-03.csv
```

## Consultas agregadas con KSQLDB

El objetivo es poder realizar consultas agregadas sobre el topic `analyzed-tweets` utilizando KSQLDB.

```bash
docker exec -it ksqldb-cli ksql http://ksqldb-server:8088
```

Creamos un stream:
```sql
CREATE STREAM tweets_stream (
    tweet_id BIGINT,
    date VARCHAR,
    username VARCHAR,
    tweet VARCHAR,
    sentiment_label VARCHAR,
    sentiment_score DOUBLE
) WITH (
    KAFKA_TOPIC='analyzed-tweets',
    VALUE_FORMAT='JSON'
);
```

Consultamos el stream:
```sql
SELECT * FROM tweets_stream EMIT CHANGES;
```

Podemos hacer el copy de los archivos para comprobar que funciona, ya que los Tweets van apareciendo en esta consulta.

Vista materializada para el conteo de sentimientos (agregación de resultados por label):
```sql
CREATE TABLE sentiment_counts AS
SELECT 
    SENTIMENT_LABEL, COUNT(*) AS count
FROM 
    tweets_stream
GROUP BY 
    SENTIMENT_LABEL;
```

Obtenemos el resultado:
```sql
SELECT * FROM sentiment_counts;
```

## Conectar con MongoDB utilizando un sink connector

**Instalar el conector en la imagen de los conectores y aplicar la configuración del conector:**

Hemos incluido las instrucciones en el ./connectors/Dockerfile y en el start.sh correspondiente.

**Iniciar la replicaset de la base de datos MongoDB:**

Hemos incluido la configuración necesaria en el docker-compose.yml. Hay que tener en cuenta que para entornos productivos sería mejor distribuir la carga en diferentes contenedores.

Por otra parte, no es necesario crear la colección porque mongo lo creará por mí.

**Ver documentos en Mongo:**

```bash
docker exec -it mongo bash
mongosh
use twitter_data
show collections
db.sentiment_tweets.find().pretty()
```

Añadir más documentos (haciendo la copia de los datos) y comprobar que aparecen en mongo volviendo a hacer `db.sentiment_tweets.find().pretty()`.



## Añadir Mongo Express

Para conectarme, hay que introducir:
- Usuario: admin
- Contraseña: pass

Dentro veremos que están los tweets en la colección `sentiment_tweets`.

Añadir más documentos (haciendo la copia de los datos) y comprobar que aparecen en mongo volviendo a hacer `db.sentiment_tweets.find().pretty()`.

## Añadir Jupyter Notebook

Creamos la carpeta `jupyter` con los archivos necesarios. También creamos el notebook `MongoDB.ipynb`.

Para entrar a Jupyter, accederemos a http://localhost:8888/. Nos solicitará un Token. El Token se debe consultar realizando:

```bash
docker exec -it jupyter bash
jupyter server list
```

Esto imprime un resultado así:
```
(base) jovyan@08c3c8660b64:~$ jupyter server list
Currently running servers:
http://08c3c8660b64:8888/?token=899207b901513ad7168a71b45b73a0bc73e8d8629bb0043d :: /home/jovyan
```

Copiar el token del URL e introducirlo en la web.