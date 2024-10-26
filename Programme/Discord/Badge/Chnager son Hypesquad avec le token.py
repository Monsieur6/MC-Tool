import requests

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
                                         
                                      ╔═════════════════════════════════════╗
                                      ║ Chnager Son Hypesquad Avec Un Token ║
                                      ╚═════════════════════════════════════╝          
"""

print(menu)

def obtenir_token_discord():
    return input("Entrez votre token Discord -> ")

def valider_token(token):
    reponse = requests.get(
        'https://discordapp.com/api/v6/users/@me',
        headers={'Authorization': token, 'Content-Type': 'application/json'}
    )
    return reponse.status_code == 200

def changer_maison_hypesquad(token, maison):
    en_tetes = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }

    map_maison = {
        "1": 1,
        "01": 1,
        "2": 2,
        "02": 2,
        "3": 3,
        "03": 3
    }

    if maison in map_maison:
        charge_utile = {'house_id': map_maison[maison]}
        reponse = requests.post(
            'https://discordapp.com/api/v6/hypesquad/online',
            headers=en_tetes,
            json=charge_utile,
            timeout=10
        )
        if reponse.status_code == 204:
            print("Maison Hypesquad changée avec succès.")
        else:
            print("Échec du changement de la maison Hypesquad.")
    else:
        print("Choix de maison invalide.")

def principal():
    token = obtenir_token_discord()
    
    if not valider_token(token):
        print("Token invalide.")
        return
    
    print("Choisissez votre Hypesquad :")
    print("1 - Bravoure")
    print("2 - Brillance")
    print("3 - Équilibre")

    maison = input("Entrez le numéro que vous voulez pour afficher votre Hypesquad -> ").strip()
    changer_maison_hypesquad(token, maison)

if __name__ == "__main__":
    principal()
