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
                                         
                                        ╔═══════════════════════════════════╗
                                        ║ Supprimer Des Amis Avec Un Token  ║
                                        ╚═══════════════════════════════════╝          
"""

print(menu)

def erreur_module(e):
    print(f"Erreur lors du chargement des modules: {e}")

def erreur_token():
    print("Le token est invalide. Veuillez vérifier et réessayer.")
    exit()

def choix_token_discord():
    return input("Veuillez entrer un token Discord -> ")

def erreur_generale(e):
    print(f"Une erreur s'est produite : {e}")

def supprimer_amis(friends, token):
    for friend in friends:
        try:
            requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}',
                            headers={'Authorization': token})
            print(f"Utilisateur supprimé: {friend['user']['username']}#{friend['user']['discriminator']}")
        except Exception as e:
            print(f"Erreur lors de la suppression : {e}")

def main():
    try:
        token = choix_token_discord()
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})

        if r.status_code != 200:
            erreur_token()

        amis = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': token}).json()

        if not amis:
            print("Aucun ami trouvé.")
            return

        processus = []
        for groupe_amis in [amis[i:i+3] for i in range(0, len(amis), 3)]:
            t = threading.Thread(target=supprimer_amis, args=(groupe_amis, token))
            t.start()
            processus.append(t)

        for process in processus:
            process.join()

        print("Tous les amis ont été supprimés avec succès.")

    except Exception as e:
        erreur_generale(e)

if __name__ == "__main__":
    main()
