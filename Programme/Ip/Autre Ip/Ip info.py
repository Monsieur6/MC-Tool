import requests

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = f"""
                                                 @@@@@@@@@@@@@@@@@@@                                 
                                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    
                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
                             @@@@@@@@@@@@@@@@@@                       @@@@@@@@@@@@@@@@@@             
                           @@@@@@@@@@@@@@                                   @@@@@@@@@@@@@@@          
                        @@@@@@@@@@@@@              @@@@@@@@@@@@@@@              @@@@@@@@@@@@@        
                       @@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@       
                       @@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@       
                        @@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@        
                                  @@@@@@@@@@@@@@@                   @@@@@@@@@@@@@@@                  
                                @@@@@@@@@@@@@                           @@@@@@@@@@@@@                
                               @@@@@@@@@@            @@@@@@@@@@@            @@@@@@@@@@               
                                @@@@@@@         @@@@@@@@@@@@@@@@@@@@@         @@@@@@@                
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                            
                                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                         @@@@@@@@@@@             @@@@@@@@@@@                         
                                        @@@@@@@@@                   @@@@@@@@@                        
                                         @@@@@@        @@@@@@@        @@@@@@                         
                                                    @@@@@@@@@@@@@                                    
                                                   @@@@@@@@@@@@@@@                                   
                                                  @@@@@@@@@@@@@@@@@                                  
                                                  @@@@@@@@@@@@@@@@@                                  
                                                   @@@@@@@@@@@@@@@                                   
                                                    @@@@@@@@@@@@@                                    
                                                       @@@@@@@    
                                                                                          
                                                     ╔═════════╗
                                                     ║ IP Info ║
                                                     ╚═════════╝                      
"""

print(menu)

ip = input("Entrez l'IP à vérifier -> ")

try:
    response = requests.get(f"http://ip-api.com/json/{ip}")
    api = response.json()

    status = "Valide" if api.get('status') == "success" else "Invalide"
    pays = api.get('country', "Non spécifié")
    code_pays = api.get('countryCode', "Non spécifié")
    region = api.get('regionName', "Non spécifié")
    code_region = api.get('region', "Non spécifié")
    code_postal = api.get('zip', "Non spécifié")
    ville = api.get('city', "Non spécifié")
    latitude = api.get('lat', "Non spécifié")
    longitude = api.get('lon', "Non spécifié")
    fuseau_horaire = api.get('timezone', "Non spécifié")
    fournisseur = api.get('isp', "Non spécifié")
    organisation = api.get('org', "Non spécifié")
    as_host = api.get('as', "Non spécifié")

except Exception as e:
    print(f"Erreur lors de la récupération des informations pour l'IP {ip}: {e}")
    status = "Erreur"
    pays = code_pays = region = code_region = code_postal = ville = latitude = longitude = fuseau_horaire = fournisseur = organisation = as_host = "Non spécifié"

print(f"""
Statut         : {status}
Pays           : {pays} ({code_pays})
Région         : {region} ({code_region})
Code postal    : {code_postal}
Ville          : {ville}
Latitude       : {latitude}
Longitude      : {longitude}
Fuseau horaire : {fuseau_horaire}
Fournisseur    : {fournisseur}
Organisation   : {organisation}
AS             : {as_host}
""")
