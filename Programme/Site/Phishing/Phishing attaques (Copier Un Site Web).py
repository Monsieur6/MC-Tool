import os
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = r"""
                                                 .+#%@@%#+.                                     
                                            .#@@@@@@@@@@@@@@@@#.                                
                                          +@@@@@@@@@@@@@@@@@@@@@@*                              
                                        .%@@@@@@@@@@@@@@@@@@@@@@@@%.                            
                                        %@@@@@@@@@@@@@@@@@@@@@@@@@@%                            
                                       %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                          
                                        -..........................-.                           
                                        %@@@@@@%%@@@@@@@@@@@%@@@@@@%                            
                                        %@@@#     .%@@@@%.     *@@@%                            
                                        . :+%%+--+%@#::#@%*--+%%+: .                            
                                                                   .                            
                                         :                        :                             
                                          -                      =                              
                                            -                  -                                
                                               -=          --                                   
                                       -+#%@@@@@@=        =@@@@@@%#+-                           
                                    *@@@@@@@@@@@@=        =@@@@@@@@@@@@*                        
                                  *@@@@@@@@@@@@@@+        +@@@@@@@@@@@@@@#                      
                                 *@@@@@@@@@@@@@@@@%=    -%@@@@@@@@@@@@@@@@#                     
                                -@@@@@@@@@@@@@@@@@@@%#*%@@@@@@@@@@@@@@@@@@@-                    
                                -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-                    
                                -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-                    
                                -@@@@@@@@@@@@@@@@@@@%::%@@@@@@@@@@@@@@@@@@@-  
                                ╔════════════════════════════════════════╗
                                ║ Phishing Attaques (Copier Un Site Web) ║
                                ╚════════════════════════════════════════╝                                                              
"""

print(menu)

try:
    site_web = input("Entrez l'URL du site web -> ")

    if "https://" not in site_web and "http://" not in site_web:
        site_web = "https://" + site_web

    def recuperer_css_js(contenu_html, url_base):
        soup = BeautifulSoup(contenu_html, 'html.parser')

        print("Récupération des fichiers CSS...")
        liens_css = soup.find_all('link', rel='stylesheet')
        tout_css = ""

        for lien in liens_css:
            url_css = urljoin(url_base, lien['href'])
            try:
                reponse_css = requests.get(url_css)
                if reponse_css.status_code == 200:
                    tout_css += reponse_css.text + "\n"
                else:
                    print("Erreur lors de la récupération du CSS.")
            except:
                print("Erreur lors de la récupération du CSS.")
        
        if tout_css:
            balise_style = soup.new_tag('style')
            balise_style.string = tout_css
            soup.head.append(balise_style)
            for lien in liens_css:
                lien.decompose()

        print("Récupération des fichiers JavaScript...")
        liens_js = soup.find_all('script', src=True)
        tout_js = ""

        for script in liens_js:
            url_js = urljoin(url_base, script['src'])
            try:
                reponse_js = requests.get(url_js)
                if reponse_js.status_code == 200:
                    tout_js += reponse_js.text + "\n"
                else:
                    print("Erreur lors de la récupération du JavaScript.")
            except:
                print("Erreur lors de la récupération du JavaScript.")
        
        if tout_js:
            balise_script = soup.new_tag('script')
            balise_script.string = tout_js
            soup.body.append(balise_script)
            for script in liens_js:
                script.decompose()

        return soup.prettify()

    print("Récupération du HTML...")
    reponse = requests.get(site_web, timeout=5)
    if reponse.status_code == 200:
        contenu_html = reponse.text
        soup = BeautifulSoup(contenu_html, 'html.parser')
        
        nom_site = re.sub(r'https?://(www\.)?', '', site_web).split('/')[0]

        dossier_sortie = os.path.join("Fichier cree", "Phishing")
        os.makedirs(dossier_sortie, exist_ok=True)

        fichier_html = os.path.join(dossier_sortie, f"{nom_site}.html")

        html_final = recuperer_css_js(contenu_html, site_web)

        with open(fichier_html, 'w', encoding='utf-8') as fichier:
            fichier.write(html_final)
        print(f"L'attaque de phishing a réussi. Le fichier se trouve dans le dossier \"{fichier_html}\"")
    else:
        print("Erreur : L'URL fournie est invalide ou inaccessible.")
except Exception as e:
    print(f"Erreur : {e}")
