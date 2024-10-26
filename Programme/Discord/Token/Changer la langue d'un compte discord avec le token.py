import requests
import time
import random

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
                                         
                                ╔═════════════════════════════════════════════════════╗
                                ║ Changer La Langue D'un Compte Discord Avec Un Token ║
                                ╚═════════════════════════════════════════════════════╝           
"""
print(menu)

def ChoisirTokenDiscord():
    return input("Veuillez entrer un token Discord -> ")

def ErreurNombre():
    print("Erreur : Vous devez entrer un nombre entier valide.")
    exit()

def Continuer():
    input("Appuyez sur Entrée pour continuer...")

def Reinitialiser():
    print("Le programme va se réinitialiser...")

def ErreurToken():
    print("Erreur : Le token Discord est invalide.")
    exit()

def Erreur(e):
    print(f"Erreur : {e}")
    exit()


try:
    token = ChoisirTokenDiscord()

    en_tetes = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=en_tetes)
    
    if r.status_code == 200:
        try:
            cycles = int(input("Combien de fois voulez-vous changer la langue ? -> "))
        except:
            ErreurNombre()

        for i in range(cycles):
            try:
                time.sleep(0.6)
                langue_aleatoire = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                parametre = {'locale': langue_aleatoire}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=en_tetes, json=parametre)
                print(f"Statut: Langue changée | Langue: {langue_aleatoire}")
            except:
                print(f"Erreur: Impossible de changer la langue | Langue: {langue_aleatoire}")
        print("\nProcessus terminé.")
        Continuer()
        Reinitialiser()
    else:
        ErreurToken()
except Exception as e:
    Erreur(e)
