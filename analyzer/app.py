#!/usr/bin/env python

import json
import avro.schema
import avro.io
from kafka import KafkaConsumer, KafkaProducer
from io import BytesIO
from transformers import pipeline
import logging


# Kafka consumer configuration
kafka_brokers = ['broker:19092']
input_topic_name = 'tweets-input'
output_topic_name = 'analyzed-tweets'

# Definir el esquema de avro esperado
avro_schema = {
  "type": "record",
  "name": "schema",
  "namespace": "tweets.input.value",
  "connect.name": "tweets.input.value.schema",
  "fields": [
    {"name": "tweet_id","type": "long"},
    {"default": None,"name": "date","type": ["null","string"]},
    {"default": None,"name": "username","type": ["null","string"]},
    {"default": None,"name": "tweet","type": ["null","string"]}
  ] 
}

# Parsear esquema
schema = avro.schema.parse(json.dumps(avro_schema))

# Iniciar el sentiment pipeline
sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

log = logging.getLogger(__name__)


# Función para decodificar el mensaje Avro
def decode_avro_message(message_value, schema):
    bytes_reader = BytesIO(message_value)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(schema)
    return reader.read(decoder)

# Funcion para el caso de exito en la produccion del metodo
def on_send_success(record_metadata):
  print(record_metadata.topic)
  print(record_metadata.partition)
  print(record_metadata.offset)

# Funcion para el caso de error
def on_send_error(ex):
  log.error('I am an Error', exc_info=ex)
  # handle exception

print("Start creating the consumer.")

# Crear el consumer
consumer = KafkaConsumer(input_topic_name,
                         group_id='py-group',
                         bootstrap_servers=kafka_brokers,
                         auto_offset_reset='earliest')

print("Consumer created. Subscription started.")

consumer.subscribe([input_topic_name])

print("Subscription created. Start creating the producer.")

# Crear el producer
producer = KafkaProducer(
    bootstrap_servers=kafka_brokers,
    value_serializer=lambda m: json.dumps(m).encode('utf-8')) # Utilizaremos la libreria JSON para serializar nuestros mensajes

print("Producer created. Start processing the messages.")

# Para cada mensaje consumido por el consumer
for message in consumer:
  # Decodificamos el mensaje y construimos el diccionario. Con [5:] eliminamos el encabezado mágico y el ID de esquema (primeros 5 bytes)
  message_dict = decode_avro_message(message.value[5:], schema)
  # Example: {'tweet_id': 2018926307, 'date': 'Wed Jun 03 10:43:39 PDT 2009', 'username': 'Mia_R', 'tweet': "@simalves LOL i was contemplating on doing the same thing Sim! but i really need to sleep... i'll stay for a few more minutes... "}
  
  # Analizamos el sentimiento del tweet
  sentiment = sentiment_pipeline([message_dict.get('tweet')])[0] # Example: {'label': 'POS', 'score': 0.5627670288085938}

  # Añadir los datos al diccionario original con nuevas claves
  message_dict['sentiment_label'] = sentiment['label']
  message_dict['sentiment_score'] = sentiment['score']
  # Example: {'tweet_id': 2018926307, 'date': 'Wed Jun 03 10:43:39 PDT 2009', 'username': 'Mia_R', 'tweet': "@simalves LOL i was contemplating on doing the same thing Sim! but i really need to sleep... i'll stay for a few more minutes... ", 'sentiment_label': 'POS', 'sentiment_score': 0.5627670288085938}

  # Imprimimos el mensaje de evento analizado
  print(f"Event analyzed: {message_dict}")

  # A traves del producer, enviamos el evento al topic de salida
  producer.send(output_topic_name, key=str(message_dict.get('tweet_id')).encode('utf-8'),
                value=message_dict).add_callback(on_send_success).add_errback(on_send_error)
  producer.flush()
  print("Event sent.")
