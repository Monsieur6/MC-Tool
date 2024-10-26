import requests
import threading

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
                                         
                                      ╔════════════════════════════════════════╗
                                      ║ Bloquer Des Amis Discord Avec Un Token ║
                                      ╚════════════════════════════════════════╝           
"""

print(menu)

def ErreurModule(e):
    print(f"Erreur du module : {e}")

def ErreurToken():
    print("Erreur de token")

def ErreurUrl():
    print("Erreur d'URL")

def Erreur(e):
    print(f"Erreur : {e}")

def Continuer():
    input("Appuyez sur Entrée pour continuer...")

def Reinitialiser():
    pass

try:
    token = input("Entrez un token Discord -> ")
    
    reponse = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if reponse.status_code != 200:
        ErreurToken()
        exit()

    def BloquerAmis(token, amis):
        for ami in amis:
            try:
                requests.put(f'https://discord.com/api/v9/users/@me/relationships/{ami["id"]}', headers={'Authorization': token}, json={"type": 2})
                print(f"Statut : Bloqué | Utilisateur : {ami['user']['username']}#{ami['user']['discriminator']}")
            except Exception as e:
                print(f"Statut : Erreur : {e}")

    liste_amis = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': token}).json()
    if not liste_amis:
        print("Aucun ami trouvé.")
        Continuer()
        Reinitialiser()
        exit()

    processus = []
    for amis_chunk in [liste_amis[i:i+3] for i in range(0, len(liste_amis), 3)]:
        t = threading.Thread(target=BloquerAmis, args=(token, amis_chunk))
        t.start()
        processus.append(t)

    for processus_thread in processus:
        processus_thread.join()

    Continuer()
    Reinitialiser()
except Exception as e:
    Erreur(e)
