import dns.resolver
import re

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = r"""                                                                             
                     q$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$B$_                    
                     $$@$@$@$@$@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$@$@$@$$$$                    
                    .$$$$$$$@$@~                                                .C$$@$$$@$@$                    
                     $$@$ ./@$$$$$W.`                                        '$$$@$@B:  $$$$                    
                     $$@$.   ..$@$$$$@'.                                  }$$$@$@@ ..   $$@$                    
                     $$@$         d$$$$$@w..                         ''@$$$@$$[         $$$$                    
                     $$@$.         '.^$$$$%$@                      ,@@$@$$@.            $@$$                    
                     $$@$              ..M$@$$$@1'             'w$$$$$$L.               $$$$                    
                    .$$@$.                . ?@$$$$@&.       .$@$$$@@"                   $$@$                    
                     $$@$                      -@$$$$$@, f8$@$$@$                       $$$$                    
                     $$@$.                   $B$$$BZ$@$@$$$$@$@$$$@                     $@$$                    
                     $$@$                .i@$$$$X      nZ{    .t$@$$$v.                 $$$$                    
                     $$@$.             '%B$@$8..                 .$$@$@$.               $$@$                    
                    .$$@$            ^$@$$Bp.                      '<@$@$@0             $$$$                    
                     $$@$.         &$@$@@.                            'B$$$$@.          $@$$                    
                     $$@$       '$$$$$#                                  l@$$$$a.       $$$$                    
                     $$@$.  ..d$$$$@^                                       B$@$$$`.    $$@$                    
                     $$@$ ' %$$$$%                                            ^B$@$@M.  $$$$                    
                    .$$$@0@$$%@l                                                 8@$$$$"@@$$                    
                     $$$$$$$B..                                                   .`$$@$$$$$                    
                     $@$@$@$@$$$@$$$$@$$$$$$$$$$$$$$$$$$$$$$$$$$$$@$$$@$$$$$$@$$$$$$$@$$@$@@                    
                     .@$$$$$$@$@$$@$$$@$@$@$@$@$@$$@$@$@$@$@$@$@$@$$@$$$@$@$@$$@$@$@$$$$$$M.                                                                      
                                    ╔═════════════════════════════════════╗
                                    ║ Chnager Son Hypesquad Avec Un Token ║
                                    ╚═════════════════════════════════════╝          
"""

print(menu)

def obtenir_info_email(email):
    info = {}
    try:
        domaine_total = email.split('@')[-1]
    except:
        domaine_total = None

    try:
        nom = email.split('@')[0]
    except:
        nom = None

    try:
        domaine = re.search(r"@([^@.]+)\.", email).group(1)
    except:
        domaine = None

    try:
        tld = f".{email.split('.')[-1]}"
    except:
        tld = None

    try:
        enregistrements_mx = dns.resolver.resolve(domaine_total, 'MX')
        serveurs_mx = [str(enregistrement.exchange) for enregistrement in enregistrements_mx]
        info["serveurs_mx"] = serveurs_mx
    except dns.resolver.NoAnswer:
        info["serveurs_mx"] = None
    except dns.resolver.NXDOMAIN:
        info["serveurs_mx"] = None

    try:
        enregistrements_spf = dns.resolver.resolve(domaine_total, 'SPF')
        info["enregistrements_spf"] = [str(enregistrement) for enregistrement in enregistrements_spf]
    except dns.resolver.NoAnswer:
        info["enregistrements_spf"] = None
    except dns.resolver.NXDOMAIN:
        info["enregistrements_spf"] = None

    try:
        enregistrements_dmarc = dns.resolver.resolve(f'_dmarc.{domaine_total}', 'TXT')
        info["enregistrements_dmarc"] = [str(enregistrement) for enregistrement in enregistrements_dmarc]
    except dns.resolver.NoAnswer:
        info["enregistrements_dmarc"] = None
    except dns.resolver.NXDOMAIN:
        info["enregistrements_dmarc"] = None

    if serveurs_mx:
        for serveur in serveurs_mx:
            if "google.com" in serveur:
                info["workspace_google"] = True
            elif "outlook.com" in serveur:
                info["microsoft_365"] = True

    return info, domaine_total, domaine, tld, nom

email = input("Entrez l'adresse e-mail -> ")
print(f"Adresse e-mail censurée : {email}")

print("Récupération des informations en cours...")
info, domaine_total, domaine, tld, nom = obtenir_info_email(email)

try:
    serveurs_mx = info["serveurs_mx"]
    serveurs_mx = ' / '.join(serveurs_mx)
except Exception as e:
    serveurs_mx = None

try:
    enregistrements_spf = info["enregistrements_spf"]
except:
    enregistrements_spf = None

try:
    enregistrements_dmarc = info["enregistrements_dmarc"]
    enregistrements_dmarc = ' / '.join(enregistrements_dmarc)
except:
    enregistrements_dmarc = None

try:
    workspace_google = info.get("workspace_google", None)
except:
    workspace_google = None

try:
    validation_mailgun = info.get("validation_mailgun", None)
    if validation_mailgun:
        validation_mailgun = ' / '.join(validation_mailgun)
except:
    validation_mailgun = None

print(f"""
Email      : {email}
Nom        : {nom}
Domaine    : {domaine}
TLD        : {tld}
Domaine Total : {domaine_total}
Serveurs    : {serveurs_mx}
SPF         : {enregistrements_spf}
DMARC       : {enregistrements_dmarc}
Workspace   : {workspace_google}
Mailgun     : {validation_mailgun}
""")

input("Appuyez sur Entrée pour quitter...")
