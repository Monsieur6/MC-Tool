import hashlib
import base64
from hashlib import pbkdf2_hmac
import bcrypt

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = r"""
                                               j@@@@@^                                 
                                          j@@@@@@@@@@@@@@@;  
                                  v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@p  
                                  v@@@@@@@@@@@@      p@@@@@@@@@@@a  
                                  |@@@@@@@@@@^ @@@@@@; @@@@@@@@@@p    
                                  >@@@@@@@@@@ p@@@@@@@ M@@@@@@@@@j     
                                   @@@@@@@@|            >@@@@@@@@; 
                                   }@@@@@@@|    O@@@    >@@@@@@@M                      
                                    @@@@@@@|     M@     >@@@@@@@^  
                                     @@@@@@|    O@@@    >@@@@@@ 
                                      @@@@@v            }@@@@@^    
                                       M@@@@@@@@@@@@@@@@@@@@@          
                                        ^@@@@@@@@@@@@@@@@@@>         
                                           @@@@@@@@@@@@@@        
                                              J@@@@@@p                         

                                  ╔══════════════════════════╗
                                  ║ Chiffrer Un Mot De Passe ║
                                  ╚══════════════════════════╝                      
"""

print(menu)

def erreur_choix():
    print("Choix invalide, veuillez réessayer.")

def continuer():
    input("Appuyez sur Entrée pour continuer...")

def erreur_generale(message):
    print(f"Une erreur est survenue : {message}")

try:
    print("Méthodes de chiffrement disponibles :")
    print("01 - BCRYPT")
    print("02 - MD5")
    print("03 - SHA-1")
    print("04 - SHA-256")
    print("05 - PBKDF2 (SHA-256)")
    print("06 - Base64")

    choix = input("Sélectionnez une méthode de chiffrement -> ")

    if choix not in ['1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06']:
        erreur_choix()
        exit()

    mot_de_passe = input("Entrez le mot de passe à chiffrer -> ")

    def chiffrer_mot_de_passe(choix, mot_de_passe):
        if choix in ['1', '01'] and bcrypt:
            try:
                sel = bcrypt.gensalt()
                mot_de_passe_chiffre = bcrypt.hashpw(mot_de_passe.encode('utf-8'), sel)
                return mot_de_passe_chiffre.decode('utf-8')
            except Exception as e:
                print(f"Erreur lors du chiffrement avec BCRYPT : {e}")
        elif choix in ['2', '02']:
            try:
                mot_de_passe_chiffre = hashlib.md5(mot_de_passe.encode('utf-8')).hexdigest()
                return mot_de_passe_chiffre
            except Exception as e:
                print(f"Erreur lors du chiffrement avec MD5 : {e}")
        elif choix in ['3', '03']:
            try:
                mot_de_passe_chiffre = hashlib.sha1(mot_de_passe.encode('utf-8')).hexdigest()
                return mot_de_passe_chiffre
            except Exception as e:
                print(f"Erreur lors du chiffrement avec SHA-1 : {e}")
        elif choix in ['4', '04']:
            try:
                mot_de_passe_chiffre = hashlib.sha256(mot_de_passe.encode('utf-8')).hexdigest()
                return mot_de_passe_chiffre
            except Exception as e:
                print(f"Erreur lors du chiffrement avec SHA-256 : {e}")
        elif choix in ['5', '05']:
            try:
                sel = "this_is_a_salt".encode('utf-8')
                mot_de_passe_chiffre = pbkdf2_hmac('sha256', mot_de_passe.encode('utf-8'), sel, 100000).hex()
                return mot_de_passe_chiffre
            except Exception as e:
                print(f"Erreur lors du chiffrement avec PBKDF2 (SHA-256) : {e}")
        elif choix in ['6', '06']:
            try:
                mot_de_passe_chiffre = base64.b64encode(mot_de_passe.encode('utf-8')).decode('utf-8')
                return mot_de_passe_chiffre
            except Exception as e:
                print(f"Erreur lors de l'encodage avec Base64 : {e}")
        else:
            return None

    mot_de_passe_chiffre = chiffrer_mot_de_passe(choix, mot_de_passe)
    if mot_de_passe_chiffre:
        print(f"Mot de passe chiffré : {mot_de_passe_chiffre}")
        continuer()
except Exception as e:
    erreur_generale(e)
