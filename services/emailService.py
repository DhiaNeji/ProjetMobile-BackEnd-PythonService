import requests
#Méthode d'envoi d'un email
def send_simple_message_new_trade(to, subject, body):
    return requests.post(
        #Utilisation de l'API Mailgun
        "https://api.mailgun.net/v3/sandbox012b878fd27947398ce114d19943a9a9.mailgun.org/messages",
        auth=("api", "d711b4ad58f60d63bec023ae2e415d61-10eedde5-acd1e81a"), #Credentials
        #Données à envoyer
        data={"from": "Mailgun Sandbox<postmaster@sandbox012b878fd27947398ce114d19943a9a9.mailgun.org>",
              "to": to,
              "subject":subject,
             "template": "justtradeittnewrequest"})