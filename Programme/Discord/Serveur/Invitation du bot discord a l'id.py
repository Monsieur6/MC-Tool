import requests
import webbrowser

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
                                         
                                        ╔════════════════════════════════════╗
                                        ║ Invitation Du Bot Discord Sont Id  ║
                                        ╚════════════════════════════════════╝        
"""

print(menu)

def afficher_erreur(message):
    print(f"Erreur : {message}")

def obtenir_id_bot():
    while True:
        try:
            id_bot = int(input("Entrez l'ID du bot Discord -> "))
            return id_bot
        except ValueError:
            afficher_erreur("ID invalide, veuillez entrer un nombre entier.")

def generer_url_invitation(id_bot):
    return f'https://discord.com/oauth2/authorize?client_id={id_bot}&scope=bot&permissions=8'

def verifier_url_invitation(url_invitation):
    try:
        reponse = requests.get(url_invitation)
        return reponse.status_code
    except requests.RequestException as e:
        afficher_erreur(f"Erreur lors de la vérification du lien : {e}")
        return None

def principal():
    id_bot = obtenir_id_bot()
    
    url_invitation = generer_url_invitation(id_bot)
    code_statut = verifier_url_invitation(url_invitation)
    
    if code_statut:
        print(f"Lien d'invitation : {url_invitation} (statut -> {code_statut})")
    
        choix = input("Souhaitez-vous ouvrir ce lien dans votre navigateur ? (y/n) -> ")
        if choix.lower() in ['o', 'oui']:
            webbrowser.open_new_tab(url_invitation)
        else:
            print("Lien non ouvert.")
    else:
        print("Impossible de vérifier le lien d'invitation.")

if __name__ == "__main__":
    try:
        principal()
    except Exception as e:
        afficher_erreur(f"Une erreur inattendue est survenue : {e}")
