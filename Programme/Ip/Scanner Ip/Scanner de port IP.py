import socket
import threading
from datetime import datetime
import queue

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

def scan_port(ip, port, result_queue):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            result_queue.put(port)

def scan_ports(ip):
    print(f"Scan des ports sur l'adresse IP : {ip}...\n")

    num_threads = 50
    result_queue = queue.Queue()
    threads = []

    for port in range(1, 1025):
        if len(threads) >= num_threads:
            for thread in threads:
                thread.join()
            threads = []
        
        thread = threading.Thread(target=scan_port, args=(ip, port, result_queue))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    open_ports = []
    while not result_queue.empty():
        open_ports.append(result_queue.get())

    if open_ports:
        print("\nPorts ouverts :")
        for port in open_ports:
            print(f"Port {port} est OUVERT")
    else:
        print("\nAucun port ouvert trouvé.")

def run():
    ip = input("Veuillez entrer l'adresse IP à scanner -> ")
    try:
        socket.inet_aton(ip)
    except socket.error:
        print(f"Erreur: Adresse IP non valide {ip}.")
        return
    
    scan_ports(ip)


if __name__ == "__main__":
    run()
