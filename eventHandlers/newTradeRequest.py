from services import emailService
#En cas d'une nouvelle demande de trading, envoyer un email
def setup_handler(channel, exchange_name):
    result_new_trade = channel.queue_declare(queue='new-trade-request',durable=True)
    queue_name_new_trade = result_new_trade.method.queue
    def callback1(ch, method, properties, body):
    #Envoyer un email via le service Email     
    emailService.send_simple_message_new_trade(body,"New Trade","New Trade").status_code
    channel.basic_consume(
    #Ecoute sur le canal
    queue=queue_name_new_trade, on_message_callback=callback1, auto_ack=True)
    

