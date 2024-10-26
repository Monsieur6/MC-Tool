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
                                         
                                ╔═════════════════════════════════════════════════════╗
                                ║ Changer Le Status D'un Compte Discord Avec Un Token ║
                                ╚═════════════════════════════════════════════════════╝           
"""
print(menu)

def gerer_erreur_module(e):
    print(f"Erreur lors de l'importation des modules : {e}")

def gerer_erreur(e):
    print(f"Erreur détectée : {e}")

def choisir_token():
    return input("Entrez un token Discord -> ")

def demander_nombre_statuts():
    while True:
        try:
            nombre = int(input("Combien de statuts souhaitez-vous changer (max 4) ? -> "))
            if 1 <= nombre <= 4:
                return nombre
            else:
                print("Veuillez entrer un nombre entre 1 et 4.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

def demander_nombre_iterations():
    while True:
        try:
            iterations = input("Combien de fois souhaitez-vous exécuter la boucle (laisser vide pour infini) ? -> ")
            if iterations == "":
                return None
            iterations = int(iterations)
            if iterations > 0:
                return iterations
            else:
                print("Veuillez entrer un nombre positif.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

def changer_statut(token, statues, iterations):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    count = 0

    while iterations is None or count < iterations:
        for statut in statues:
            payload = {"custom_status": {"text": statut}}
            try:
                response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
                if response.status_code == 200:
                    print(f"Statut changé en : {statut}")
                else:
                    print(f"Erreur lors du changement de statut : {response.status_code}")
                time.sleep(5)
            except Exception as e:
                print(f"Erreur lors de la requête : {e}")
                time.sleep(5)
        count += 1

def main():
    try:
        token = choisir_token()
        nombre_statuts = demander_nombre_statuts()
        statues = []

        for i in range(nombre_statuts):
            statut = input(f"Entrez le statut personnalisé {i + 1} -> ")
            statues.append(statut)

        iterations = demander_nombre_iterations()
        changer_statut(token, statues, iterations)

    except Exception as e:
        gerer_erreur(e)

if __name__ == "__main__":
    main()
