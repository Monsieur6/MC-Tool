import requests
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
                                         
                                ╔══════════════════════════════════════════════════════╗
                                ║ Quitter Un Ou Plusieur Serveur Discord Avec Un Token ║
                                ╚══════════════════════════════════════════════════════╝           
"""
print(menu)

def quitter_serveur(guilds, token, tout_quitter=False):
    if tout_quitter:
        for serveur in guilds:
            quitter_un_serveur(serveur, token)
    else:
        print("\nVoici la liste des serveurs ->")
        for index, serveur in enumerate(guilds):
            print(f"{index + 1}. {serveur['name']}")
        
        choix = input("\nEntrez le(s) numéro(s) du/des serveur(s) à quitter (séparés par une virgule) ou 'tous' pour quitter tous les serveurs -> ").strip().lower()
        if choix == 'tous':
            for serveur in guilds:
                quitter_un_serveur(serveur, token)
        else:
            indices = choix.split(',')
            for indice in indices:
                try:
                    serveur = guilds[int(indice) - 1]
                    quitter_un_serveur(serveur, token)
                except (IndexError, ValueError):
                    print(f"Numéro de serveur invalide : {indice}")

def quitter_un_serveur(serveur, token):
    try:
        response = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{serveur["id"]}', headers={'Authorization': token})
        if response.status_code in [200, 204]:
            print(f"Vous avez quitté le serveur : {serveur['name']}")
        else:
            print(f"Erreur lors du départ du serveur {serveur['name']} (code: {response.status_code})")
    except Exception as e:
        print(f"Erreur lors du traitement du serveur {serveur['name']}: {e}")

token = input("Veuillez entrer votre token Discord -> ").strip()

try:
    response = requests.get("https://discord.com/api/v8/users/@me/guilds", headers={'Authorization': token})
    if response.status_code == 200:
        guilds = response.json()
        if not guilds:
            print("Aucun serveur trouvé.")
        else:
            tout_quitter = input("Souhaitez-vous quitter tous les serveurs ? (oui/non) -> ").strip().lower() == 'oui'
            quitter_serveur(guilds, token, tout_quitter)
    else:
        print("Erreur : token invalide ou problème de connexion.")
except Exception as e:
    print(f"Erreur lors de la récupération des serveurs : {e}")
