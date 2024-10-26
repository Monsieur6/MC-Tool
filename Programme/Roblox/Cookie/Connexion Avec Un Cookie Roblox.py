import sys
import time
from selenium import webdriver
                                                                                      
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
                    ╔═════════════════════════════════╗
                    ║ Connexion Avec Un Cookie Roblox ║
                    ╚═════════════════════════════════╝          
"""

print(menu)                                                                                         
    
try:
    cookie = input("\nVeuillez entrer un cookie Roblox -> ")
    print("""
    01. Chrome (Windows / Linux)
    02. Edge (Windows)
    03. Firefox (Windows)
    """)
    
    navigateur = input("Veuillez sélectionner votre navigateur (1, 2, ou 3) -> ")

    if navigateur in ['1', '01']:
        try:
            nom_navigateur = "Chrome"
            print(f"Lancement de {nom_navigateur}...")
            driver = webdriver.Chrome()
            print(f"{nom_navigateur} prêt !")
        except Exception as e:
            print(f"Erreur : {nom_navigateur} n'est pas installé ou le driver n'est pas à jour. {e}")
            input("Appuyez sur Entrée pour quitter...")
            exit()

    elif navigateur in ['2', '02']:
        if sys.platform.startswith("linux"):
            print("Edge n'est pas supporté sur Linux.")
            input("Appuyez sur Entrée pour quitter...")
            exit()
        else:
            try:
                nom_navigateur = "Edge"
                print(f"Lancement de {nom_navigateur}...")
                driver = webdriver.Edge()
                print(f"{nom_navigateur} prêt !")
            except Exception as e:
                print(f"Erreur : {nom_navigateur} n'est pas installé ou le driver n'est pas à jour. {e}")
                input("Appuyez sur Entrée pour quitter...")
                exit()

    elif navigateur in ['3', '03']:
        if sys.platform.startswith("linux"):
            print("Firefox n'est pas supporté sur Linux.")
            input("Appuyez sur Entrée pour quitter...")
            exit()
        else:
            try:
                nom_navigateur = "Firefox"
                print(f"Lancement de {nom_navigateur}...")
                driver = webdriver.Firefox()
                print(f"{nom_navigateur} prêt !")
            except Exception as e:
                print(f"Erreur : {nom_navigateur} n'est pas installé ou le driver n'est pas à jour. {e}")
                input("Appuyez sur Entrée pour quitter...")
                exit()
    else:
        print("Choix de navigateur invalide.")
        input("Appuyez sur Entrée pour quitter...")
        exit()
    
    try:
        driver.get("https://www.roblox.com/Login")
        print("Connexion via le cookie en cours...")
        driver.add_cookie({"name": ".ROBLOSECURITY", "value": f"{cookie}"})
        print("Cookie ajouté avec succès !")
        print("Actualisation de la page...")
        driver.refresh()
        print("Connecté avec succès !")
        time.sleep(1)
        driver.get("https://www.roblox.com/users/profile")
        print(f"Si vous fermez cet outil, {nom_navigateur} se fermera également.")
        
        input("Appuyez sur Entrée pour fermer la fenêtre...")

    except Exception as e:
        print(f"Erreur lors de la connexion : {e}")
        input("Appuyez sur Entrée pour quitter...")

except Exception as e:
    print(f"Erreur générale : {e}")
    input("Appuyez sur Entrée pour quitter...")
