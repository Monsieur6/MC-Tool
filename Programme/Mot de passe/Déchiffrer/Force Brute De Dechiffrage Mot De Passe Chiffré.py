import bcrypt
import hashlib
import base64
from hashlib import pbkdf2_hmac
import random
import string
import threading

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = r"""
                                 ^M@@@@@@@@@v                                    
                              v@@@@@@@@@@@@@@@@@                                 
                            _@@@@@@@}    ;a@@@@@@@                               
                           M@@@@@            @@@@@@                              
                          ;@@@@@              O@@@@@                             
                          @@@@@v               @@@@@                             
                          @@@@@;               @@@@@                             
                          @@@@@;                                                 
                          @@@@@;        v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
                                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
                                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                     @@@@@@@@@@@@@@@@j     @@@@@@@@@@@@@@@@      
                                     @@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@      
                                     @@@@@@@@@@@@@@@v       @@@@@@@@@@@@@@@      
                                     @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                     @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                     @@@@@@@@@@@@@@@@@_   @@@@@@@@@@@@@@@@@      
                                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|      
                                       ^@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O     
                                                                                      
                        ╔══════════════════════════════════════════════════════╗
                        ║ Force Brute De Déchiffrage D'un Mot De Passe Chiffré ║
                        ╚══════════════════════════════════════════════════════╝                      
"""

print(menu)

def detecter_chiffrement(mot_de_passe_chiffre):
    if mot_de_passe_chiffre.startswith("$2b$") or mot_de_passe_chiffre.startswith("$2a$"):
        return "BCRYPT"
    elif len(mot_de_passe_chiffre) == 32:
        return "MD5"
    elif len(mot_de_passe_chiffre) == 40:
        return "SHA-1"
    elif len(mot_de_passe_chiffre) == 64:
        return "SHA-256"
    elif len(mot_de_passe_chiffre) > 64:
        return "PBKDF2"
    try:
        base64.b64decode(mot_de_passe_chiffre.encode('utf-8'))
        return "Base64"
    except:
        return None

def erreur_chiffrement(methode):
    print(f"Erreur : le mot de passe chiffré ne correspond pas à la méthode détectée : {methode}.")

def verifier_mot_de_passe(mot_de_passe_test, mot_de_passe_chiffre, methode):
    if methode == "BCRYPT":
        try:
            return bcrypt.checkpw(mot_de_passe_test.encode('utf-8'), mot_de_passe_chiffre.encode('utf-8'))
        except:
            erreur_chiffrement(methode)
    elif methode == "MD5":
        return hashlib.md5(mot_de_passe_test.encode('utf-8')).hexdigest() == mot_de_passe_chiffre
    elif methode == "SHA-1":
        return hashlib.sha1(mot_de_passe_test.encode('utf-8')).hexdigest() == mot_de_passe_chiffre
    elif methode == "SHA-256":
        return hashlib.sha256(mot_de_passe_test.encode('utf-8')).hexdigest() == mot_de_passe_chiffre
    elif methode == "PBKDF2":
        sel = "this_is_a_salt".encode('utf-8')
        return pbkdf2_hmac('sha256', mot_de_passe_test.encode('utf-8'), sel, 100000).hex() == mot_de_passe_chiffre
    elif methode == "Base64":
        try:
            return base64.b64decode(mot_de_passe_chiffre.encode('utf-8')).decode('utf-8') == mot_de_passe_test
        except:
            erreur_chiffrement(methode)
    return False

def generer_mot_de_passe():
    tous_les_caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(tous_les_caracteres) for _ in range(random.randint(1, 12)))

def tester_mot_de_passe(mot_de_passe_chiffre, methode):
    mot_de_passe_trouve = False
    mots_de_passe_genérés = set()

    while not mot_de_passe_trouve:
        mot_de_passe_test = generer_mot_de_passe()
        if mot_de_passe_test not in mots_de_passe_genérés:
            mots_de_passe_genérés.add(mot_de_passe_test)
            if verifier_mot_de_passe(mot_de_passe_test, mot_de_passe_chiffre, methode):
                mot_de_passe_trouve = True
                print(f"Mot de passe trouvé : {mot_de_passe_test}")

def brute_force(mot_de_passe_chiffre, nombre_threads):
    methode = detecter_chiffrement(mot_de_passe_chiffre)
    if not methode:
        print("Erreur : méthode de chiffrement inconnue.")
        return
    
    print(f"Méthode détectée : {methode}")
    threads = []
    
    for _ in range(nombre_threads):
        t = threading.Thread(target=tester_mot_de_passe, args=(mot_de_passe_chiffre, methode))
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    mot_de_passe_chiffre = input("Entrez le mot de passe chiffré -> ")
    nombre_threads = int(input("Entrez le nombre de threads à utiliser -> "))
    brute_force(mot_de_passe_chiffre, nombre_threads)
