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
                                              
                                                  ╔══════════════╗
                                                  ║ Webhook Info ║
                                                  ╚══════════════╝     
"""

print(menu)

def info_webhook(webhook_url):
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(webhook_url, headers=headers)

        if response.status_code == 429:
            retry_after = response.json().get('retry_after', 1)
            print(f"Erreur 429 : Trop de requêtes. Attendre {retry_after} secondes...")
            time.sleep(retry_after)
            return info_webhook(webhook_url)

        if response.status_code != 200:
            print(f"Erreur : Statut de la réponse {response.status_code}. Vérifiez l'URL du Webhook.")
            return
        
        try:
            webhook_info = response.json()
        except ValueError:
            print("Erreur lors du décodage de la réponse JSON. La réponse peut être vide ou non valide.")
            print(f"Contenu de la réponse : {response.text}")
            return

    except requests.RequestException as e:
        print(f"Une erreur est survenue lors de la requête : {e}")
        return

    webhook_id = webhook_info.get('id', "Aucun")
    webhook_token = webhook_info.get('token', "Aucun")
    webhook_name = webhook_info.get('name', "Aucun")
    webhook_avatar = webhook_info.get('avatar', "Aucun")
    webhook_type = "bot" if webhook_info.get('type') == 1 else "webhook utilisateur"
    channel_id = webhook_info.get('channel_id', "Aucun")
    guild_id = webhook_info.get('guild_id', "Aucun")

    print(f"""
    ID         : {webhook_id}
    Token      : {webhook_token}
    Nom        : {webhook_name}
    Avatar     : {webhook_avatar}
    Type       : {webhook_type}
    ID du Canal : {channel_id}
    ID du Serveur : {guild_id}
    """)

    if 'user' in webhook_info:
        user_info = webhook_info['user']
        
        user_id = user_info.get('id', "Aucun")
        username = user_info.get('username', "Aucun")
        display_name = user_info.get('global_name', "Aucun")
        discriminator = user_info.get('discriminator', "Aucun")
        user_avatar = user_info.get('avatar', "Aucun")
        user_flags = user_info.get('flags', "Aucun")
        accent_color = user_info.get('accent_color', "Aucun")
        avatar_decoration = user_info.get('avatar_decoration_data', "Aucun")
        banner_color = user_info.get('banner_color', "Aucun")

        print(f"""
        Informations utilisateur associées au Webhook :
        ID          : {user_id}
        Nom         : {username}
        Nom d'affichage : {display_name}
        Numéro      : {discriminator}
        Avatar      : {user_avatar}
        Drapeaux    : {user_flags}
        Couleur     : {accent_color}
        Décoration  : {avatar_decoration}
        Bannière    : {banner_color}
        """)

try:
    webhook_url = input("\nEntrez l'URL du Webhook : ")
    info_webhook(webhook_url)
except Exception as e:
    print(f"Une erreur est survenue : {e}")
