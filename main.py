import os
import subprocess
from colorama import Fore, Style, init

def set_console_title(title):
    subprocess.run(['title', title], shell=True)

def init_colorama():
    init(autoreset=True)
    os.system('color 4')

def print_red(text):
    print(Fore.RED + text)

set_console_title("MC")

banner = f"""
                                                             /$$      /$$  /$$$$$$ 
                                                            | $$$    /$$$ /$$__  $$ 
                                                            | $$$$  /$$$$| $$  \__/
                                                            | $$ $$/$$ $$| $$ 
                                                            | $$  $$$| $$| $$    $$ 
                                                            | $$\  $ | $$| $$    $$ 
                                                            | $$ \/  | $$|  $$$$$$/ 
                                                            |__/     |__/ \______/ 
                                                        https://github.com/Monsieur6
                                                              ┌────────────────┐
                                                              │ Menu Principal │
                                                              └────────────────┘
"""
choix = f"""                                                                [p2] = Page 2
  ┌─────────────┐         ┌──────────┐         ┌────────┐         ┌────────────┐         ┌────────────┐
┌─┤ [1] Discord │       ┌─┤ [2] Site │       ┌─┤ [3] IP │       ┌─┤ [4] Pseudo │       ┌─┤ [5] Roblox │
│ └─────────────┘       │ └──────────┘       │ └────────┘       │ └────────────┘       │ └────────────┘"""

choix2 = f"""                                                                [p1] = Page 1
  ┌───────────┐         ┌──────────────────┐         ┌─────────────────────────┐
┌─┤ [6] Email │       ┌─┤ [7] Mot De Passe │       ┌─┤ [8] Recherche Des Infos │
│ └───────────┘       │ └──────────────────┘       │ └─────────────────────────┘"""


discord_menu = f"""├─ Nitro                                  
│  └─ [1] Gen Nitro + Verification  
├─ Serveur                                         
│  ├─ [2] Invitation Du Bot Discord Sont Id                                           
│  ├─ [3] Serveur Discord Info 
│  ├─ [4] Gen Des Webhooks + le Verification
│  ├─ [5] Supprimer Une Webhook
│  ├─ [6] Spammer Des Message Avec Une Webhook
│  └─ [7] Info Sur Une Webhook  
├─ Token                     
│  ├─ [8] Token info     
│  ├─ [9] Connexion Avec Un Token Discord                            
│  ├─ [10] Gen Token + Verification                              
│  ├─ [11] Supprime Les Dm Discord Avec Un Token
│  ├─ [12] Supprimer Des Amis Avec Un Token
│  ├─ [13] Bloquer Des Amis Discord Avec Un Token
│  ├─ [14] Changer La Langue D'un Compte Discord Avec Un Token
│  ├─ [15] Changer Le Status D'un Compte Discord Avec Un Token
│  ├─ [16] Quitter Un Ou Plusieur Serveur Discord Avec Un Token 
│  ├─ [17] Envoyer Un ou Plusieur Message A Tout Le Monde En Dm Avec Un Token
│  ├─ [18] Détruire Un Compte Discord Avec Un Token 
│  └─ [19] Trouver Le Token D'un Compte Discord Avec Sont Id (En Mode Brute Force)
└─ Badge
   └─ [20] Changer Son Hypesquad Avec Un Token

[0] Retour au Menu Principal
"""

site_menu = f"""                        ├─ Analyser
                        │  ├─ [1] Analyseur Les vulnérabilités D'un Site
                        ├─ Scan
                        │  └─ [2] Scanner Les Informations Sur Un Site Web
                        └─ Phishing
                           └─ [3] Phishing Attaques (Copier Un Site Web)

[0] Retour au Menu Principal
"""

ip_menu = f"""                                             ├─ Scan
                                             │  ├─ [1] Scanner De Port IP
                                             │  └─ [2] Scanner IP
                                             └─ Autre
                                                ├─ [3] Gen IP + Verification
                                                ├─ [4] IP Info
                                                └─ [5] Ping IP

[0] Retour au Menu Principal
"""

pseudo_menu = f"""                                                                └─ Tracker
                                                                   └─ [1] Tracker Un Pseudo

[0] Retour au Menu Principal
"""

roblox_menu = f"""                                                                                         ├─ Cookie
                                                                                         │  └─ [1] Connexion Avec Un Cookie Roblox
                                                                                         └─ Info               
                                                                                            ├─ [2] Info D'un Compte Roblox Avec Sont ID Roblox
                                                                                            └─ [3] Info D'un Compte Roblox Avec Sont Nom D'utilisateur

[0] Retour au Menu Principal
"""

email_menu = f"""└─ Lookup
   └─ [1] Lookup Une Adresse Mail

[0] Retour au Menu Principal
"""

mot_de_passe_menu = f"""                      ├─ Chiffrement 
                      │  └─ [1] Chiffrer Un Mot De Passe
                      └─ Déchiffrage 
                         └─ [2] Force Brute De Déchiffrage D'un Mot De Passe Chiffré

[0] Retour au Menu Principal
"""

recherche_info_basse_de_donnee_menu = f"""                                                   └─ Recherche
                                                      └─ [1] Recherche Des Infos Dans Une Basse De Donnée

[0] Retour au Menu Principal
"""


menus = {
    1: discord_menu,
    2: site_menu,
    3: ip_menu,
    4: pseudo_menu,
    5: roblox_menu,
    6: email_menu,
    7: mot_de_passe_menu,
    8: recherche_info_basse_de_donnee_menu,
}

scripts = {
    '1_1': 'Programme\\Discord\\Nitro\\Gen nitro + verification.py',
    '1_2': 'Programme\\Discord\\Serveur\\Invitation du bot discord a l\'id.py',
    '1_3': 'Programme\\Discord\\Serveur\\Serveur discord info.py',
    '1_4': 'Programme\\Discord\\Serveur\\Webhook Gen.py',
    '1_5': 'Programme\\Discord\\Serveur\\Webhook supprimer.py',
    '1_6': 'Programme\\Discord\\Serveur\\Spam Webhook.py',
    '1_7': 'Programme\\Discord\\Serveur\\Webhook info.py',
    '1_8': 'Programme\\Discord\\Token\\Token info.py',
    '1_9': 'Programme\\Discord\\Token\\Connexion Avec Un Token Discord.py',
    '1_10': 'Programme\\Discord\\Token\\Gen token + verification.py',
    '1_11': 'Programme\\Discord\\Token\\Supprime dm discord avec le token.py',
    '1_12': 'Programme\\Discord\\Token\\Supprimer des amis avec le token.py',
    '1_13': 'Programme\\Discord\\Token\\Bloquer d\'amis discord avec le token.py',
    '1_14': 'Programme\\Discord\\Token\\Changer la langue d\'un compte discord avec le token.py',
    '1_15': 'Programme\\Discord\\Token\\Changer le status d\'un compte discord avec un token.py',
    '1_16': 'Programme\\Discord\\Token\\Quitter serveur discord avec un token.py',
    '1_17': 'Programme\\Discord\\Token\\Envoyer un message a tout le personne en dm avec un token.py',
    '1_18': 'Programme\\Discord\\Token\\Détruire un compte discord avec un token.py',
    '1_19': 'Programme\\Discord\\Token\\Trouver le token d\'un compte avec sont id.py',
    '1_20': 'Programme\\Discord\\Badge\\Chnager son Hypesquad avec le token.py',
    
    '2_1': 'Programme\\Site\\Analyser\\Analyseur de vulnérabilités site.py',
    '2_2': 'Programme\\Site\\Scanner\\Scanner d\'informations sur le site web.py',
    '2_3': 'Programme\\Site\\Phishing\\Phishing attaques (Copier Un Site Web).py',

    '3_1': 'Programme\\Ip\Scanner Ip\\Scanner de port IP.py',
    '3_2': 'Programme\\Ip\\Scanner Ip\\Scanner Ip.py',
    '3_3': 'Programme\\Ip\\Autre Ip\\Gen Ip + verification.py',
    '3_4': 'Programme\\Ip\\Autre Ip\\Ip info.py',
    '3_5': 'Programme\\Ip\\Autre Ip\\Ping Ip.py',

    '4_1': 'Programme\\Pseudo\\Recherhce\\Tracker Un Pseudo.py',

    '5_1': 'Programme\\Roblox\\Cookie\\Connexion Avec Un Cookie Roblox.py',
    '5_2': 'Programme\\Roblox\\Info\\Info D\'un Compte Roblox Avec Sont ID.py',
    '5_3': 'Programme\\Roblox\\Info\\Info D\'un Compte Roblox Avec Sont Nom D\'utilisateur.py',

    '6_1': 'Programme\\Email\\Lookup\\Lookup Une Adresse Mail.py',

    '7_1': 'Programme\\Mot de passe\\Chiffrage\\Chiffrer Un Mot De Passe.py',
    '7_2': 'Programme\\Mot de passe\\Déchiffrer\\Force Brute De Dechiffrage Mot De Passe Chiffré.py',

    '8_1': 'Programme\\Recherche des info dans une basse de données\\Recherche Des Info Dans Une Basse De Données.py',
}

def display_menu(submenu=None, page='1'):
    os.system('cls')
    print_red(banner)
    
    if page == '1':
        print_red(choix)
        if submenu:
            print_red(submenu)
    elif page == '2':
        print_red(choix2)
        if submenu:
            print_red(submenu)

def open_script(script_path):
    subprocess.run(f'start cmd /k python "{script_path}"', shell=True)

while True:
    display_menu()

    try:
        choice = input(f'\nChoix: ').strip()

        if choice in ['6', '7', '8']:
            print_red("Choix invalide. Vous ne pouvez pas faire ces choix en page 1.")
            continue

        if choice == 'p2':
            while True:
                display_menu(page='2')
                page2_choice = input(f'\nChoix page 2: ').strip()

                if page2_choice == 'p1':
                    break
                
                if page2_choice == '0':
                    print_red('Vous avez choisi de quitter les sous-choix.')
                    break

                if page2_choice in ['1', '2', '3', '4', '5',]:
                    print_red("Choix invalide. Vous ne pouvez pas faire ces choix en page 2.")
                    continue

                if page2_choice == '6':
                    display_menu(email_menu, page='2')
                    submenu_choice = int(input(f'Sous-choix: '))

                    if submenu_choice == 0:
                        print_red('Vous avez choisi de quitter les sous-choix.')
                        continue

                    script_key = f'6_{submenu_choice}'
                    script = scripts.get(script_key)

                    if script:
                        open_script(script)
                    else:
                        print_red('Sous-choix invalide.')

                    input(f'Appuyez sur Entrée pour continuer...')

                if page2_choice == '7':
                    display_menu(mot_de_passe_menu, page='2')
                    submenu_choice = int(input(f'Sous-choix: '))

                    if submenu_choice == 0:
                        print_red('Vous avez choisi de quitter les sous-choix.')
                        continue

                    script_key = f'7_{submenu_choice}'
                    script = scripts.get(script_key)

                    if script:
                        open_script(script)
                    else:
                        print_red('Sous-choix invalide.')

                    input(f'Appuyez sur Entrée pour continuer...')

                elif page2_choice == '8':
                    display_menu(recherche_info_basse_de_donnee_menu, page='2')
                    submenu_choice = int(input(f'Sous-choix: '))

                    if submenu_choice == 0:
                        print_red('Vous avez choisi de quitter les sous-choix.')
                        continue

                    script_key = '8_1'
                    script = scripts.get(script_key)

                    if script:
                        open_script(script)
                    else:
                        print_red('Sous-choix invalide.')

        elif choice.isdigit():
            choice = int(choice)
            if choice in menus:
                while True:
                    display_menu(menus[choice])
                    submenu_choice = int(input(f'Sous-choix: '))

                    if submenu_choice == 0:
                        break

                    script_key = f'{choice}_{submenu_choice}'
                    script = scripts.get(script_key)

                    if script:
                        open_script(script)
                    else:
                        print_red('Sous-choix invalide.')

                    input(f'Appuyez sur Entrée pour continuer...')
            else:
                print_red('Choix invalide.')
        else:
            print_red('Entrée invalide. Veuillez entrer un numéro ou "p" pour passer à la page 2.')

    except ValueError:
        print_red('Entrée invalide. Veuillez entrer un numéro.')
