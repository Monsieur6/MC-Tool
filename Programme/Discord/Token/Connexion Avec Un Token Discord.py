import sys
import time
from selenium import webdriver

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
                                         
                                        ╔═════════════════════════════════╗
                                        ║ Connexion Avec Un Token Discord ║
                                        ╚═════════════════════════════════╝           
"""
print(menu)

def ChoisirTokenDiscord():
    return input("Entrez un token Discord -> ")

def Continuer():
    input("Appuyez sur Entrée pour continuer...")

def Réinitialiser():
    print("Réinitialisation de l'outil...")

def SeulementLinux():
    print("Ce script ne peut pas être exécuté sur Linux avec ce navigateur.")

def ErreurChoix():
    print("Erreur : Choix de navigateur invalide.")

def Erreur(e):
    print(f"Erreur : {e}")


try:      
    token = ChoisirTokenDiscord()

    print(f"""
 1 - Chrome (Windows / Linux)
 2 - Edge (Windows)
 3 - Firefox (Windows)
    """)
    navigateur = input("Choisissez votre navigateur -> ")
 
    if navigateur in ['1', '01']:
        try:
            print("Démarrage de Chrome...")
            driver = webdriver.Chrome()
            print("Chrome prêt !")
        except Exception as e:
            print("Erreur : Chrome n'est pas installé ou le driver n'est pas à jour.")
            Continuer()
            Réinitialiser()

    elif navigateur in ['2', '02']:
        if sys.platform.startswith("linux"):
            SeulementLinux()
        else:
            try:
                print("Démarrage de Edge...")
                driver = webdriver.Edge()
                print("Edge prêt !")
            except Exception as e:
                print("Erreur : Edge n'est pas installé ou le driver n'est pas à jour.")
                Continuer()
                Réinitialiser()

    elif navigateur in ['3', '03']:
        if sys.platform.startswith("linux"):
            SeulementLinux()
        else:
            try:
                print("Démarrage de Firefox...")
                driver = webdriver.Firefox()
                print("Firefox prêt !")
            except Exception as e:
                print("Erreur : Firefox n'est pas installé ou le driver n'est pas à jour.")
                Continuer()
                Réinitialiser()
    else:
        ErreurChoix()
    
    try:
        script = """
            function connexion(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
        
        driver.get("https://discord.com/login")
        print("Connexion avec le token en cours...")
        driver.execute_script(script + f'\nconnexion("{token}")')
        time.sleep(4)
        print("Token connecté avec succès !")
        print("Si vous quittez l'outil, le navigateur se fermera !")
        Continuer()
        Réinitialiser()
    except Exception as e:
        print("Erreur : Problème lors de la connexion.")
        Continuer()
        Réinitialiser()
except Exception as e:
    Erreur(e)
