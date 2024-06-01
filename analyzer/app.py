from transformers import pipeline
sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

# Solicitar tres cadenas de texto al usuario
tweet1 = input("Ingresa el primer tweet: ")
tweet2 = input("Ingresa el segundo tweet: ")
tweet3 = input("Ingresa el tercer tweet: ")

array_of_tweets = [tweet1, tweet2, tweet3]

print("Estoy analizando tus Tweets, en seguida te digo su mood ;)")
print(sentiment_pipeline(array_of_tweets))