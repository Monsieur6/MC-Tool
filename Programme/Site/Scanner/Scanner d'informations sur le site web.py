import socket
import concurrent.futures
import requests
from urllib.parse import urlparse
import ssl
import urllib3
from requests.exceptions import RequestException
import time
import re
import dns.resolver
from bs4 import BeautifulSoup
import whois

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = r"""
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                   >|a@@@@@@@@@|                                                
                                              }@@@@@@@@@@@@@@@@| 000M|                                          
                                          ;@@@@@@O  @@@@@@@@@@@|  j000000_                                      
                                       }@@@@@v   |@@@@@@@@@@@@@| 00J  |00000j                                   
                                     @@@@@_     @@@@@@@@@@@@@@@| 0000    ;00000^                                
                                  ;@@@@v       _@@@@@@@     >@@| 0000v      }0000_                              
                                ^@@@@_         @@@@@@@      ^O@| 00000        ;0000_                            
                                 @@@@;         @@@@@@@      ;p@| 00000         0000^                            
                                   @@@@p       >@@@@@@@^    >@@| 0000v      J0000;                              
                                     O@@@@|     M@@@@@@@@@@@@@@| 0000    >00000                                 
                                       ;@@@@@J^  }@@@@@@@@@@@@@| 00v  j00000}                                   
                                          >@@@@@@@_;@@@@@@@@@@@| ;M000000_                                      
                                              >@@@@@@@@@@@@@@@@| 00000}                                          
                                                   ^jpM@@@@@@@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@| 
                                                            
                                        ╔══════════════════════════════════════════╗
                                        ║ Scanner Les Informations Sur Un Site Web ║
                                        ╚══════════════════════════════════════════╝                      
"""

print(menu)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def trouver_url_site(url):
    if not urlparse(url).scheme:
        url_site = "https://" + url
    else:
        url_site = url
    print(f"Site Web : {url_site}")
    return url_site

def domaine_site(url_site):
    parsed_url = urlparse(url_site)
    domaine = parsed_url.netloc
    print(f"Domaine : {domaine}")
    return domaine

def ip_site(domaine):
    try:
        ip = socket.gethostbyname(domaine)
    except socket.gaierror:
        ip = "Aucune"
    print(f"IP : {ip}")
    return ip

def type_ip(ip):
    if ':' in ip:
        type_ip = "ipv6"
    elif '.' in ip:
        type_ip = "ipv4"
    else:
        type_ip = "Inconnu"
    print(f"Type d'IP : {type_ip}")

def site_securise(url_site):
    securise = url_site.startswith("https://")
    print(f"Sécurisé : {securise}")

def statut_site(url_site):
    try:
        reponse = requests.get(url_site, timeout=5)
        code_statut = reponse.status_code
    except RequestException:
        code_statut = 404
    print(f"Code de Statut : {code_statut}")

def info_ip(ip):
    url_api = f"https://ipinfo.io/{ip}/json"
    try:
        reponse = requests.get(url_api)
        api = reponse.json()
    except RequestException:
        api = {}

    pays_hote = api.get('country', 'Aucun')
    print(f"Pays Hôte : {pays_hote}")

    nom_hote = api.get('hostname', 'Aucun')
    print(f"Nom Hôte : {nom_hote}")

    isp_hote = api.get('isp', 'Aucun')
    print(f"ISP Hôte : {isp_hote}")

    org_hote = api.get('org', 'Aucun')
    print(f"Organisation Hôte : {org_hote}")

    as_hote = api.get('asn', 'Aucun')
    print(f"AS Hôte : {as_hote}")

def dns_ip(ip):
    try:
        dns, _, _ = socket.gethostbyaddr(ip)
    except:
        dns = "Aucun"
    print(f"DNS Hôte : {dns}")

def ports_site(ip):
    map_protocole_ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
        80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
        443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
        1521: "Oracle DB", 3389: "RDP"
    }

    liste_ports = [21, 22, 23, 25, 53, 69, 80, 110, 123, 143, 194, 389, 443, 161, 3306, 5432, 6379, 1521, 3389]

    def scanner_port(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultat = sock.connect_ex((ip, port))
            if resultat == 0:
                protocole = identifier_protocole(ip, port)
                print(f"Port : {port} Statut : Ouvert Protocole : {protocole}")
            sock.close()
        except:
            pass

    def identifier_protocole(ip, port):
        try:
            if port in map_protocole_ports:
                return map_protocole_ports[port]
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((ip, port))
                
                sock.send(b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode('utf-8'))
                reponse = sock.recv(100).decode('utf-8')
                if "HTTP" in reponse:
                    return "HTTP"

                sock.send(b"\r\n")
                reponse = sock.recv(100).decode('utf-8')
                if "FTP" in reponse:
                    return "FTP"

                sock.send(b"\r\n")
                reponse = sock.recv(100).decode('utf-8')
                if "SSH" in reponse:
                    return "SSH"

                return "Inconnu"
        except:
            return "Inconnu"

    with concurrent.futures.ThreadPoolExecutor() as executor:
        resultats = {executor.submit(scanner_port, ip, port): port for port in liste_ports}
    concurrent.futures.wait(resultats)

def entetes_http(url_site):
    try:
        reponse = requests.get(url_site, timeout=5)
        entetes = reponse.headers
        for entete, valeur in entetes.items():
            print(f"Entête HTTP : {entete} Valeur : {valeur}")
    except RequestException:
        pass

def verifier_certificat_ssl(url_site):
    try:
        contexte = ssl.create_default_context()
        with contexte.wrap_socket(socket.socket(), server_hostname=urlparse(url_site).hostname) as sock:
            sock.settimeout(5)
            sock.connect((urlparse(url_site).hostname, 443))
            cert = sock.getpeercert()
        for cle, valeur in cert.items():
            print(f"Clé Certificat SSL : {cle} Valeur : {valeur}")
    except:
        pass

def verifier_entetes_securite(url_site):
    entetes_interessants = ['Content-Security-Policy', 'Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection']
    try:
        reponse = requests.get(url_site, timeout=5)
        entetes = reponse.headers
        for entete in entetes_interessants:
            if entete in entetes:
                print(f"Entête de Sécurité : {entete} Valeur : {entetes[entete]}")
            else:
                print(f"Entête de Sécurité Manquant : {entete}")
    except RequestException:
        pass

def analyser_cookies(url_site):
    try:
        reponse = requests.get(url_site, timeout=5)
        cookies = reponse.cookies
        for cookie in cookies:
            secure = 'Sécurisé' if cookie.secure else 'Non Sécurisé'
            httponly = 'HttpOnly' if cookie.has_nonstandard_attr('HttpOnly') else 'Non HttpOnly'
            print(f"Cookie : {cookie.name} Sécurisé : {secure} HttpOnly : {httponly}")
    except RequestException:
        pass

def verifier_redirections(url_site):
    try:
        reponse = requests.get(url_site, timeout=5, allow_redirects=True)
        if reponse.history:
            for resp in reponse.history:
                print(f"Redirections : {resp.url} Statut : {resp.status_code}")
            print(f"Redirections : {reponse.url} Statut : {reponse.status_code}")
        else:
            print("Pas de redirections")
    except RequestException:
        pass

def verifier_entetes_http_additionnels(url_site):
    try:
        reponse = requests.get(url_site, timeout=5)
        entetes = reponse.headers
        entetes_additionnels = ['Server', 'X-Powered-By', 'X-UA-Compatible', 'X-Permitted-Cross-Domain-Policies']
        for entete in entetes_additionnels:
            if entete in entetes:
                print(f"Entête Additionnel : {entete} Valeur : {entetes[entete]}")
            else:
                print(f"Entête Additionnel Manquant : {entete}")
    except RequestException:
        pass

def tester_performance(url_site):
    try:
        temps_debut = time.time()
        reponse = requests.get(url_site, timeout=10)
        temps_fin = time.time()
        temps_reponse = temps_fin - temps_debut
        print(f"Temps de Réponse : {temps_reponse:.2f} secondes")
        print(f"Taille de la Réponse : {len(reponse.content)} octets")
    except RequestException:
        pass

def analyser_contenu(url_site):
    try:
        reponse = requests.get(url_site, timeout=5)
        contenu = reponse.text
        correspondance_titre = re.search(r'<title>(.*?)</title>', contenu, re.IGNORECASE)
        if correspondance_titre:
            titre = correspondance_titre.group(1)
            print(f"Titre de la Page : {titre}")
        else:
            print("Titre de la Page : Non trouvé")

        soup = BeautifulSoup(contenu, 'html.parser')
        meta_description = soup.find('meta', attrs={'name': 'description'})
        if meta_description:
            description = meta_description.get('content', 'Aucune')
            print(f"Meta Description : {description}")
        else:
            print("Meta Description : Non trouvée")
    except RequestException:
        pass

def recherche_whois(domaine):
    try:
        info_domaine = whois.whois(domaine)
        for cle, valeur in info_domaine.items():
            print(f"WHOIS {cle} : {valeur}")
    except Exception as e:
        print(f"Échec de la Recherche WHOIS : {e}")

def verifier_enregistrements_dns(domaine):
    types_enregistrements = ['A', 'AAAA', 'MX', 'CNAME', 'NS', 'SOA']
    for type_enregistrement in types_enregistrements:
        try:
            reponses = dns.resolver.resolve(domaine, type_enregistrement)
            for reponse in reponses:
                print(f"{type_enregistrement} : {reponse.to_text()}")
        except dns.resolver.NoAnswer:
            print(f"{type_enregistrement} : Aucun")
        except dns.resolver.NoNameservers:
            print(f"{type_enregistrement} : Serveur DNS introuvable")
        except dns.exception.DNSException as e:
            print(f"{type_enregistrement} : Erreur DNS {e}")

def main():
    url = input("Entrez l'URL du site web : ").strip()
    url_site = trouver_url_site(url)
    domaine = domaine_site(url_site)
    ip = ip_site(domaine)
    type_ip(ip)
    site_securise(url_site)
    statut_site(url_site)
    info_ip(ip)
    dns_ip(ip)
    ports_site(ip)
    entetes_http(url_site)
    verifier_certificat_ssl(url_site)
    verifier_entetes_securite(url_site)
    analyser_cookies(url_site)
    verifier_redirections(url_site)
    verifier_entetes_http_additionnels(url_site)
    tester_performance(url_site)
    analyser_contenu(url_site)
    recherche_whois(domaine)
    verifier_enregistrements_dns(domaine)

if __name__ == "__main__":
    main()
