from os import times
from connection.queueConnection import setup
from eventHandlers import newTradeRequest, tradeStatusUpdate
import time
import sys

import services
if __name__ == "__main__":
    #Initialisation du service
    channel, connection, exchange_name = setup()
    newTradeRequest.setup_handler(channel, exchange_name)
    channel.start_consuming()
    connection.close()
    