import requests

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = r"""                                                                                           
                        q$$$Zt"                                                          
                       .$$$$$$$$$$$$$L,.                                                 
                       8$$$$$$$$$$$$$$$$$$$$$kz,                                         
                      {$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$O}"                                
                      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%Q"                        
                     O$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$dx:               
                    `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'          
                    Z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$L           
                   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$            
                   #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$1            
                  _$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%             
                  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$_             
                 U$$$$$$$$$$$$$$$$$$$$$${ `[$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$              
                `$$$$$$$$$$$$$$$$$$$$$$$           a$$$$$$$$$$$$$$$$$$$$$$,              
                Z$$$$$$$$$$$$$$$$$$$$$$+          >$$$$$$$$$$$$$$$$$$$$$$m               
               `$$$$$$$$$$$$$$$$$$$$$$$           $$$$$$$$$$$$$$$$$$$$$$$                
               a$$$$$$$$$$$$$$$$$$$$$$,          Q$$$$$$$$$$$$$$$$$$$$$$(                
              !$$$$$$$$$$$$$$$$$$$$$$$$$$$$1^   ^$$$$$$$$$$$$$$$$$$$$$$8                 
              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$+                 
             n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$8                  
            '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;                  
            Z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$k                   
           "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                    
           d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$/                    
             .[O$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%                     
                      'z8$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>                     
                              ^}L$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&                      
                                       :La$$$$$$$$$$$$$$$$$$$$$$$$I                      
                                               'i*$$$$$$$$$$$$$$$W                       
                                                        !n*$$$$$$                        
          ╔═════════════════════════════════════════════════════╗
          ║ Info D'un Compte Roblox Avec Sont Nom D'utilisateur ║
          ╚═════════════════════════════════════════════════════╝          
"""

print(menu)  

def Continue():
    input("Appuyez sur Entrée pour continuer...")

def Reset():
    print("\nTout a été réinitialisé.")

def ErrorUsername():
    print("Erreur : Le nom d'utilisateur est invalide ou n'existe pas.")

def Error(e):
    print(f"Une erreur est survenue : {e}")

try:
    nom_utilisateur = input("Veuillez entrer le nom d'utilisateur roblox  -> ")
    print("Récupération des informations en cours...")

    try:
        response = requests.post("https://users.roblox.com/v1/usernames/users", json={
            "usernames": [nom_utilisateur],
            "excludeBannedUsers": "true"
        })

        data = response.json()

        if not data['data']:
            print("Aucun utilisateur trouvé avec ce nom.")
        else:
            user_id = data['data'][0]['id']

            response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
            api = response.json()

            userid = api.get('id', "Inconnu")
            nom_affichage = api.get('displayName', "Inconnu")
            username = api.get('name', "Inconnu")
            description = api.get('description', "Inconnu")
            cree_le = api.get('created', "Inconnu")
            est_banni = api.get('isBanned', "Inconnu")
            nom_externe = api.get('externalAppDisplayName', "Inconnu")
            a_badge_verifie = api.get('hasVerifiedBadge', "Inconnu")

            print(f"""
            Nom d'utilisateur    : {username}
            ID                   : {userid}
            Nom d'affichage      : {nom_affichage}
            Description          : {description}
            Créé le              : {cree_le}
            Banni                : {est_banni}
            Nom externe          : {nom_externe}
            Badge vérifié        : {a_badge_verifie}
            """)

            Continue()
            Reset()
    except Exception as e:
        ErrorUsername()
except Exception as e:
    Error(e)
