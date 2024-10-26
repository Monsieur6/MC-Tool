import socket
import time

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
                                                                                          
                                                     ╔═════════╗
                                                     ║ Ping IP ║
                                                     ╚═════════╝                      
"""

print(menu)

def afficher_erreur(message):
    print(f"[ERREUR] {message}")

def afficher_informations(message):
    print(f"[INFO] {message}")

def ping_ip(hote, port, taille):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        debut = time.time() 
        sock.connect((hote, port))
        donnees = b'\x00' * taille
        sock.sendall(donnees)
        fin = time.time() 
        temps_ecoule = (fin - debut) * 1000 
        print(f"[{time.strftime('%H:%M:%S')}] Hôte: {hote} Temps: {temps_ecoule:.2f}ms Port: {port} Taille: {taille} Status: succès")
    except:
        temps_ecoule = 0
        print(f"[{time.strftime('%H:%M:%S')}] Hôte: {hote} Temps: {temps_ecoule}ms Port: {port} Taille: {taille} Status: échec")

def main():
    try:
        hote = input("Entrez l'adresse IP à analyser -> ")

        try:
            port_input = input("Entrez le port (laisser vide pour défaut) -> ")
            if port_input.strip():
                port = int(port_input)
            else:
                port = 80  
            
            taille_input = input("Entrez la taille (laisser vide pour défaut) -> ")
            if taille_input.strip():
                taille = int(taille_input)
            else:
                taille = 64
        except ValueError:
            afficher_erreur("Valeur incorrecte pour le port ou la taille.")
            return

        while True:
            ping_ip(hote, port, taille)
            time.sleep(1)

    except Exception as e:
        afficher_erreur(str(e))

if __name__ == "__main__":
    main()
