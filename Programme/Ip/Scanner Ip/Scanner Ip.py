import requests
import subprocess
import socket
import sys
import ssl
import concurrent.futures

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
                                                            
                                                   ╔════════════════════╗
                                                   ║ Scanner De Port IP ║
                                                   ╚════════════════════╝                      
"""

print(menu)

def ip_type(ip):
    if ':' in ip:
        ip_type = "ipv6"
    elif '.' in ip:
        ip_type = "ipv4"
    else:
        ip_type = "Inconnu"
        return
    print(f"[{current_time_hour()}] Type d'IP : {ip_type}")

def ip_ping(ip):
    try:
        if sys.platform.startswith("win"):
            result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=1)
        else:
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=1)
        ping_status = "Réussi" if result.returncode == 0 else "Échoué"
    except:
        ping_status = "Échoué"
    
    print(f"[{current_time_hour()}] Ping : {ping_status}")

def ip_port(ip):
    port_protocol_map = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
        80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
        443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
        1521: "Oracle DB", 3389: "RDP"
    }

    port_list = port_protocol_map.keys()

    def scan_port(ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    protocol = port_protocol_map.get(port, "Inconnu")
                    print(f"[{current_time_hour()}] Port {port} est OUVERT (Protocole : {protocol})")
        except:
            pass

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {executor.submit(scan_port, ip, port): port for port in port_list}
    concurrent.futures.wait(results)

def ip_dns(ip):
    try:
        dns, _, _ = socket.gethostbyaddr(ip)
    except:
        dns = "Aucun"
    
    if dns != "Aucun":
        print(f"[{current_time_hour()}] DNS : {dns}")

def ip_host_info(ip):
    api_url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(api_url)
        api_data = response.json()
    except requests.RequestException:
        api_data = {}

    host_country = api_data.get('country', 'Non disponible')
    host_name = api_data.get('hostname', 'Non disponible')
    host_isp = api_data.get('isp', 'Non disponible')
    host_as = api_data.get('as', 'Non disponible')

    print(f"[{current_time_hour()}] Pays de l'hôte : {host_country}")
    print(f"[{current_time_hour()}] Nom de l'hôte : {host_name}")
    print(f"[{current_time_hour()}] FAI : {host_isp}")
    print(f"[{current_time_hour()}] Système autonome : {host_as}")

def ssl_certificate_check(ip):
    port = 443
    try:
        context = ssl.create_default_context()
        with socket.create_connection((ip, port), timeout=1) as sock:
            with context.wrap_socket(sock, server_hostname=ip) as ssock:
                cert = ssock.getpeercert()
                print(f"[{current_time_hour()}] Certificat SSL : {cert}")
    except Exception as e:
        print(f"[{current_time_hour()}] Échec de la vérification SSL : {e}")

def current_time_hour():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

def run_scan():
    ip = input("Veuillez entrer l'adresse IP à scanner -> ")
    print(f"[{current_time_hour()}] Récupération des informations pour l'IP : {ip}\n")

    ip_type(ip)
    ip_ping(ip)
    ip_dns(ip)
    ip_port(ip)
    ip_host_info(ip)
    ssl_certificate_check(ip)

if __name__ == "__main__":
    run_scan()
