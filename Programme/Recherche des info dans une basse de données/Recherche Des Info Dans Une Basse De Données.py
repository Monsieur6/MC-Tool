import os

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = r"""
                                                                                   ^                      
                                                                                 J@@M                     
                                                                        ^         @@@@^                   
                                                                     ;@@@>         J@@@                   
                                                                      ;@@@J      ;j j@@@}                 
                                                                       ^@@@O  ^J@@@@^;@@@}                
                                                                   >@@@; @@@@^;@@@@@> ;@@@O               
                                                                >j _@@@@j p@@@^;@|      @@@>              
                                                              }@@@@  @@@@j J@@@>                          
                                                          ^a@@ _@@@@;_@@@@a }@@@>                         
                                                       ^} v@@@@^;@@@@@@@@@@@ >@@@v                        
                                                     |@@@@ ^@@@@J@@@@@@@@@@@@;^@@@J                       
                                                  J@M }@@@@ _@@@@@@@@@@@@@@j    @@j                       
                                               ; v@@@@ >@@@@@@@@@@@@@@@@j                                 
                                            ^@@@@ ;@@@@v@@@@@@@@@@@@@j^                                   
                                            a@@@@@ >@@@@@@@@@@@@@@a                                       
                                            |@@@@@@@@@@@@@@@@@@J                                          
                                          |a ;@@@@@@@@@@@@@@a;                                            
                                         @@@@ ;@@@@@@@@@@@;                                               
                                        |@@@@@> @@@@@@@>                                                  
                                     }@@@pO@MJ   >pp_                                                     
                                  ;@@@a                                                                   
                               ;@@@p;                                                                     
                            >p@@M>                                                                        
                           }@@>                  
                                ╔══════════════════════════════════════════════╗
                                ║ Recherche Des Infos Dans Une Basse De Donnée ║
                                ╚══════════════════════════════════════════════╝                                                              
"""

print(menu)

def Continue():
    print("Appuyez sur Entrée pour continuer...")
    input()

def Reset():
    print("Réinitialisation des paramètres...")

def Error(e):
    print(f"Une erreur s'est produite : {e}")

try:
    dossier_base_de_donnees_relative = "DataBase"
    dossier_base_de_donnees = os.path.abspath(dossier_base_de_donnees_relative)

    print(f"""
Ajoutez la base de données dans le dossier "{dossier_base_de_donnees_relative}".""")

    recherche = input("Recherche -> ")

    print("Recherche dans la base de données...")

    try:
        fichiers_recherches = 0

        def verifier(dossier):
            global fichiers_recherches
            resultats_trouves = False
            print(f"Recherche dans {dossier}...")
            for element in os.listdir(dossier):
                chemin_element = os.path.join(dossier, element)

                if element == "Info.txt":
                    continue

                if os.path.isdir(chemin_element):
                    resultats_trouves |= verifier(chemin_element)
                elif os.path.isfile(chemin_element):
                    try:
                        with open(chemin_element, 'r', encoding='utf-8') as fichier:
                            numero_ligne = 0
                            fichiers_recherches += 1
                            for ligne in fichier:
                                numero_ligne += 1
                                if recherche in ligne:
                                    resultats_trouves = True
                                    ligne_info = ligne.strip().replace(recherche, recherche)
                                    print(f"""
- Dossier : {dossier}
- Fichier : {element}
- Ligne   : {numero_ligne}
- Résultat : {ligne_info}
    """)
                    except UnicodeDecodeError:
                        try:
                            with open(chemin_element, 'r', encoding='latin-1') as fichier:
                                fichiers_recherches += 1
                                numero_ligne = 0
                                for ligne in fichier:
                                    numero_ligne += 1
                                    if recherche in ligne:
                                        resultats_trouves = True
                                        ligne_info = ligne.strip().replace(recherche, recherche)
                                        print(f"""
- Dossier : {dossier}
- Fichier : {element}
- Ligne   : {numero_ligne}
- Résultat : {ligne_info}
    """)
                        except Exception as e:
                            print(f"Erreur lors de la lecture du fichier \"{element}\": {e}")
                    except Exception as e:
                        print(f"Erreur lors de la lecture du fichier \"{element}\": {e}")
            return resultats_trouves

        resultats_trouves = verifier(dossier_base_de_donnees)
        if not resultats_trouves:
            print(f"Aucun résultat trouvé pour \"{recherche}\".")

        print(f"Total de fichiers recherchés : {fichiers_recherches}")

    except Exception as e:
        print(f"Erreur durant la recherche : {e}")

    Continue()
    Reset()
except Exception as e:
    Error(e)
