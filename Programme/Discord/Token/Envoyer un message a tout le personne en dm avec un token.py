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
                                         
                        ╔════════════════════════════════════════════════════════════════════╗
                        ║ Envoyer Un ou Plusieur Message A Tout Le Monde En Dm Avec Un Token ║
                        ╚════════════════════════════════════════════════════════════════════╝           
"""
print(menu)

def envoyer_message_masse(token_discord, canaux, message):
    for canal in canaux:
        for utilisateur in [x["username"] + "#" + x["discriminator"] for x in canal["recipients"]]:
            try:
                response = requests.post(
                    f"https://discord.com/api/v9/channels/{canal['id']}/messages",
                    headers={'Authorization': token_discord},
                    data={"content": message}
                )
                if response.status_code == 200:
                    print(f'Statut: Envoyé | Utilisateur: {utilisateur}')
                else:
                    print(f'Statut: Erreur lors de l\'envoi à {utilisateur}: {response.text}')
            except Exception as e:
                print(f'Statut: Erreur: {e}')

try:
    token_discord = input("Entrez votre token Discord -> ")
    
    validite_test = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token_discord})
    if validite_test.status_code != 200:
        print("Token invalide.")
        exit()

    message = input("Message à envoyer -> ")
    
    repetition = int(input("Nombre de répétitions -> "))
    
    canaux = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token_discord}).json()

    for i in range(repetition):
        if not canaux:
            print("Aucun canal trouvé.")
            break
        
        threads = []
        for canal in [canaux[i:i+3] for i in range(0, len(canaux), 3)]:
            thread = threading.Thread(target=envoyer_message_masse, args=(token_discord, canal, message))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        print(f"Fin de la répétition n°{i + 1}.")
        
except Exception as e:
    print(f"Une erreur est survenue: {e}")
