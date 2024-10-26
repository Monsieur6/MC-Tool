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
                ╔══════════════════════════════════════╗
                ║ Info D'un Compte Roblox Avec Sont ID ║
                ╚══════════════════════════════════════╝          
"""

print(menu)     

def afficher_erreur(erreur):
    print(f"Erreur : {erreur}")

def continuer():
    input("Appuyez sur Entrée pour continuer...")

def reinitialiser():
    print("Réinitialisation terminée.")

try:
    user_id = input("Veuillez entrer l'ID utilisateur roblox -> ")
    print("Récupération des informations en cours...")

    try:
        response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        api = response.json()

        userid = api.get('id', "Non disponible")
        nom_affiche = api.get('displayName', "Non disponible")
        nom_utilisateur = api.get('name', "Non disponible")
        description = api.get('description', "Non disponible")
        date_creation = api.get('created', "Non disponible")
        est_banni = api.get('isBanned', "Non disponible")
        nom_app_externe = api.get('externalAppDisplayName', "Non disponible")
        badge_verifie = api.get('hasVerifiedBadge', "Non disponible")

        print(f"""
        Nom d'utilisateur : {nom_utilisateur}
        ID : {userid}
        Nom affiché : {nom_affiche}
        Description : {description}
        Date de création : {date_creation}
        Banni : {est_banni}
        Nom externe : {nom_app_externe}
        Badge vérifié : {badge_verifie}
        """)

        continuer()
        reinitialiser()
    
    except:
        print("Erreur : ID utilisateur non valide ou problème de récupération des informations.")
except Exception as e:
    afficher_erreur(e)
