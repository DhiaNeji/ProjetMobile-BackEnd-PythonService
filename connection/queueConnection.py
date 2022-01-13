import pika
import os

#Nom de l'échange
exchange_name = 'JustTradeItExchange'

def setup():
    #On utilise le localHost car l'instance RabbitMQ est installée sur PC local
    #Création de la connexion et écoute
    queue_host = os.environ.get('QUEUE_HOST') or 'localhost'
    connection = pika.BlockingConnection(pika.ConnectionParameters(queue_host, credentials=pika.PlainCredentials('guest', 'guest')))
    channel = connection.channel()
    # Declare the exchange, if it doesn't exist
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)

    return (
        channel,
        connection,
        exchange_name
    )