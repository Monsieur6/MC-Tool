import random
import threading
import subprocess
import sys
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = f"""
                                                 @@@@@@@@@@@@@@@@@@@                                 
                                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    
                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
                             @@@@@@@@@@@@@@@@@@                       @@@@@@@@@@@@@@@@@@             
                           @@@@@@@@@@@@@@                                   @@@@@@@@@@@@@@@          
                        @@@@@@@@@@@@@              @@@@@@@@@@@@@@@              @@@@@@@@@@@@@        
                       @@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@       
                       @@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@       
                        @@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@        
                                  @@@@@@@@@@@@@@@                   @@@@@@@@@@@@@@@                  
                                @@@@@@@@@@@@@                           @@@@@@@@@@@@@                
                               @@@@@@@@@@            @@@@@@@@@@@            @@@@@@@@@@               
                                @@@@@@@         @@@@@@@@@@@@@@@@@@@@@         @@@@@@@                
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                            
                                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                         @@@@@@@@@@@             @@@@@@@@@@@                         
                                        @@@@@@@@@                   @@@@@@@@@                        
                                         @@@@@@        @@@@@@@        @@@@@@                         
                                                    @@@@@@@@@@@@@                                    
                                                   @@@@@@@@@@@@@@@                                   
                                                  @@@@@@@@@@@@@@@@@                                  
                                                  @@@@@@@@@@@@@@@@@                                  
                                                   @@@@@@@@@@@@@@@                                   
                                                    @@@@@@@@@@@@@                                    
                                                       @@@@@@@        
                                                                                      
                                              ╔═══════════════════════╗
                                              ║ Gen IP + Verification ║
                                              ╚═══════════════════════╝                      
"""

print(menu)

nombre_valides = 0
nombre_invalides = 0
nombre_erreurs = 0

dossier_ip = "Fichier cree/IP"

if not os.path.exists(dossier_ip):
    os.makedirs(dossier_ip)

def verifier_ip(ip: str) -> str:
    global nombre_erreurs
    try:
        if sys.platform.startswith("win"):
            result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=1)
        elif sys.platform.startswith("linux"):
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=1)
        else:
            print("Système d'exploitation non pris en charge")
            return "Erreur"

        if result.returncode == 0:
            return "Valide"
        else:
            return "Invalide"
    except Exception:
        nombre_erreurs += 1
        return "Erreur"

def generer_ip() -> str:
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def verifier_ip_thread():
    global nombre_valides, nombre_invalides, nombre_erreurs
    ip = generer_ip()
    statut = verifier_ip(ip)
    if statut == "Valide":
        chemin_fichier = os.path.join(dossier_ip, "Gen_Ip_qui_marche.txt")
        with open(chemin_fichier, "a") as fichier:
            fichier.write(f"{ip}\n")
        nombre_valides += 1
    elif statut == "Invalide":
        nombre_invalides += 1
    elif statut == "Erreur":
        nombre_erreurs += 1

def executer_verifications():
    global nombre_valides, nombre_invalides, nombre_erreurs
    nombre_threads = 50

    with ThreadPoolExecutor(max_workers=nombre_threads) as executor:
        futures = [executor.submit(verifier_ip_thread) for _ in range(nombre_threads)]
        for future in as_completed(futures):
            pass

def main():
    while True:
        global nombre_valides, nombre_invalides, nombre_erreurs
        nombre_valides = 0
        nombre_invalides = 0
        nombre_erreurs = 0

        executer_verifications()
        
        print(f"\nIP qui marche -> {nombre_valides}")
        print(f"IP qui marche pas -> {nombre_invalides}")
        print(f"Erreurs -> {nombre_erreurs}")
        
        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
