from transformers import pipeline
from kafka import KafkaConsumer

sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

# Solicitar tres cadenas de texto al usuario
# tweet1 = input("Ingresa el primer tweet: ")
# tweet2 = input("Ingresa el segundo tweet: ")
# tweet3 = input("Ingresa el tercer tweet: ")

# array_of_tweets = [tweet1, tweet2, tweet3]

# print("Estoy analizando tus Tweets, en seguida te digo su mood ;)")
# print(sentiment_pipeline(array_of_tweets))



consumer = KafkaConsumer('tweets-input',
                         group_id='input-group',
                         bootstrap_servers=['127.0.0.1:9092'],
                         auto_offset_reset='earliest')

consumer.subscribe(['tweets-input'])

for message in consumer:
  # message value and key are raw bytes -- decode if necessary!
  # e.g., for unicode: `message.value.decode('utf-8')`
  print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                       message.offset,
                                       message.key.decode('utf-8'),
                                       message.value.decode('latin-1')))