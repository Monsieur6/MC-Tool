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
                                      ║ Supprime Les Dm Discord Avec Un Token  ║
                                      ╚════════════════════════════════════════╝       
"""

print(menu)

def afficher_erreur_module(erreur):
    print(f"Erreur du module : {erreur}")

def afficher_erreur_token():
    print("Erreur du token")

def afficher_erreur(erreur):
    print(f"Erreur : {erreur}")

def continuer():
    input("Appuyez sur Entrée pour continuer...")

def reinitialiser():
    pass

def obtenir_token_discord():
    return input("Veuillez entrer un token Discord -> ")

def obtenir_nom_utilisateur(token, canal_id):
    try:
        reponse = requests.get(f'https://discord.com/api/v7/channels/{canal_id}', headers={'Authorization': token})
        reponse_json = reponse.json()
        if 'recipient' in reponse_json:
            utilisateur = reponse_json['recipient']
            return f"{utilisateur['username']}#{utilisateur['discriminator']}"
        elif 'recipients' in reponse_json:
            utilisateurs = [f"{util['username']}#{util['discriminator']}" for util in reponse_json['recipients']]
            return ', '.join(utilisateurs)
        return "Inconnu"
    except Exception as e:
        return f"Erreur : {e}"

def supprimer_dms(token, canaux):
    for canal in canaux:
        try:
            nom_utilisateur = obtenir_nom_utilisateur(token, canal['id'])
            requests.delete(f'https://discord.com/api/v7/channels/{canal["id"]}', headers={'Authorization': token})
            print(f"Statut : Supprimé | Canal : {canal['id']} | Utilisateur : {nom_utilisateur}")
        except Exception as e:
            print(f"Statut : Erreur : {e}")

try:
    token = obtenir_token_discord()
    
    reponse = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if reponse.status_code != 200:
        afficher_erreur_token()
        continuer()
        reinitialiser()
        exit()

    reponse_canaux = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token})
    canaux = reponse_canaux.json()

    if not canaux:
        print("Aucun message direct trouvé.")
        continuer()
        reinitialiser()
        exit()

    processus = []
    for groupe_canaux in [canaux[i:i+3] for i in range(0, len(canaux), 3)]:
        t = threading.Thread(target=supprimer_dms, args=(token, groupe_canaux))
        t.start()
        processus.append(t)
    
    for processus_thread in processus:
        processus_thread.join()

    continuer()
    reinitialiser()

except Exception as e:
    afficher_erreur(e)
