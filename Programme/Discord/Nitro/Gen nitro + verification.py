import random
import string
import json
import requests
import threading
import os
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
                                         
                                            ╔══════════════════════════╗
                                            ║ Gen Nitro + Verification ║
                                            ╚══════════════════════════╝                      
"""

print(menu)

invalid_count = 0
valid_count = 0

def generer_code_nitro():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

def afficher_counters():
    sys.stdout.write(f"\rInvalide : {invalid_count} | Valide : {valid_count}")
    sys.stdout.flush()

def verifier_nitro(code_nitro, webhook_url=None):
    global invalid_count, valid_count
    url_nitro = f'https://discord.gift/{code_nitro}'
    try:
        response = requests.get(f'https://discord.com/api/v9/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)
        if response.status_code == 200:
            valid_count += 1
            afficher_counters()
            enregistrer_nitro_valide(url_nitro)
            if webhook_url:
                envoyer_webhook(webhook_url, url_nitro)
        else:
            invalid_count += 1
            afficher_counters()
    except requests.RequestException as e:
        print(f"\nErreur lors de la vérification : {e}")

def enregistrer_nitro_valide(url_nitro):
    dossier = os.path.join("Fichier cree", "Discord")
    fichier_path = os.path.join(dossier, "Nitro valide.txt")

    if not os.path.exists(dossier):
        os.makedirs(dossier)

    with open(fichier_path, "a") as fichier:
        fichier.write(f"Valide : {url_nitro}\n")
    print(f"\nLien valide enregistré dans {fichier_path}")

def envoyer_webhook(webhook_url, url_nitro):
    payload = {
        'embeds': [({
            'title': 'Nitro Valide!',
            'description': f"**Nitro:**\n{url_nitro}",
            'color': 65280
        })],
        'username': 'Nitro Bot'
    }

    headers = {'Content-Type': 'application/json'}
    try:
        requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    except requests.RequestException as e:
        print(f"\nErreur lors de l'envoi au webhook : {e}")

def executer_verification(threads_number, webhook_url=None):
    def worker():
        while True:
            code_nitro = generer_code_nitro()
            verifier_nitro(code_nitro, webhook_url)

    threads = []
    for _ in range(threads_number):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    utiliser_webhook = input("Voulez-vous utiliser un webhook ? (y/n) : ").lower()
    webhook_url = None
    if utiliser_webhook == 'y':
        webhook_url = input("Entrez l'URL du webhook : ")

    try:
        threads_number = int(input("Nombre de threads : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        exit()

    executer_verification(threads_number, webhook_url)
