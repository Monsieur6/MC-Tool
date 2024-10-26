import requests
from datetime import datetime, timezone

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = f"""
                                              @@@@                @%@@                                      
                                       @@@@@@@@@@@@               @@@@@@@@@@%                               
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                         
                                %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                    
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                          %@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@%                  
                          %@@@@@@@@@@@@@@@@        %@@@@@@@@@@@%@        @@@@@@@@@@@@@@@@@                  
                          %@@@@@@@@@@@@@@@          @@@@@@@@@@@@          @@@@@@@@@@@@@@@%                  
                         %@@@@@@@@@@@@@@@@          @@@@@@@@@@@%          %@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@%         @@@@@@@@@@@%         %@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@      %@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@%                 
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                           @%@@@@@@@@@@@@@%@@   @@@@%@@@@@@@@@%%%@%@@  @@@@@@@@@@@@@@@@@@                   
                              @@%@@@@@@@@@@@@@                        @%@@@@@@@@@@@%@@                      
                                   @%@@@@@@@                            @@@@@@%%@                           
                                         @@                              @@     
                                         
                                                    ╔═════════════╗
                                                    ║ Token info  ║
                                                    ╚═════════════╝ 
"""

print(menu)

def obtenir_token_discord():
    token = input("Entrez un token Discord -> ")
    return token

def recuperer_informations_utilisateur(token_discord):
    try:
        api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()

        reponse = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})
        statut = "Valide" if reponse.status_code == 200 else "Invalide"

        nom_utilisateur_discord = api.get('username', "Aucun") + '#' + api.get('discriminator', "Aucun")
        nom_affichage_discord = api.get('global_name', "Aucun")
        id_utilisateur_discord = api.get('id', "Aucun")
        email_discord = api.get('email', "Aucun")
        email_verifie_discord = api.get('verified', "Aucun")
        telephone_discord = api.get('phone', "Aucun")
        mfa_discord = api.get('mfa_enabled', "Aucun")
        pays_discord = api.get('locale', "Aucun")
        avatar_discord = api.get('avatar', "Aucun")
        decoration_avatar_discord = api.get('avatar_decoration_data', "Aucun")
        drapeaux_publics_discord = api.get('public_flags', "Aucun")
        drapeaux_discord = api.get('flags', "Aucun")
        bannière_discord = api.get('banner', "Aucun")
        couleur_bannière_discord = api.get('banner_color', "Aucun")
        couleur_accent_discord = api.get("accent_color", "Aucun")
        nsfw_discord = api.get('nsfw_allowed', "Aucun")

        try:
            cree_le_discord = datetime.fromtimestamp(((int(api.get('id', 'Aucun')) >> 22) + 1420070400000) / 1000, timezone.utc)
        except:
            cree_le_discord = "Aucun"

        try:
            nitro_discord = {
                0: 'Non',
                1: 'Nitro Classic',
                2: 'Nitro Boosts',
                3: 'Nitro Basic'
            }.get(api.get('premium_type', 'Aucun'), 'Non')
        except:
            nitro_discord = "Aucun"

        try:
            url_avatar_discord = f"https://cdn.discordapp.com/avatars/{id_utilisateur_discord}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{id_utilisateur_discord}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{id_utilisateur_discord}/{api['avatar']}.png"
        except:
            url_avatar_discord = "Aucun"
        
        try:
            utilisateurs_lies_discord = api.get('linked_users', 'Aucun')
            utilisateurs_lies_discord = ' / '.join(utilisateurs_lies_discord) if utilisateurs_lies_discord else "Aucun"
        except:
            utilisateurs_lies_discord = "Aucun"
        
        try:
            bio_discord = api.get('bio', 'Aucun')
            bio_discord = bio_discord if bio_discord and not bio_discord.isspace() else "Aucun"
        except:
            bio_discord = "Aucun"
        
        try:
            types_authentificateurs_discord = api.get('authenticator_types', 'Aucun')
            types_authentificateurs_discord = ' / '.join(types_authentificateurs_discord) if types_authentificateurs_discord else "Aucun"
        except:
            types_authentificateurs_discord = "Aucun"

        try:
            reponse_guilds = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token_discord})
            if reponse_guilds.status_code == 200:
                guilds = reponse_guilds.json()
                nombre_guilds = len(guilds)
                guilds_proprietaire = [guild for guild in guilds if guild['owner']]
                nombre_guilds_proprietaire = f"({len(guilds_proprietaire)})"
                noms_guilds_proprietaire = "\n".join(f"{guild['name']} ({guild['id']})" for guild in guilds_proprietaire) if guilds_proprietaire else "Aucun"
            else:
                nombre_guilds_proprietaire = "Aucun"
                nombre_guilds = "Aucun"
                noms_guilds_proprietaire = "Aucun"
        except:
            nombre_guilds_proprietaire = "Aucun"
            nombre_guilds = "Aucun"
            noms_guilds_proprietaire = "Aucun"

        try:
            facturation_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token_discord}).json()
            methodes_paiement_discord = []
            if facturation_discord:
                for methode in facturation_discord:
                    if methode['type'] == 1:
                        methodes_paiement_discord.append('CB')
                    elif methode['type'] == 2:
                        methodes_paiement_discord.append("Paypal")
                    else:
                        methodes_paiement_discord.append('Autre')
                methodes_paiement_discord = ' / '.join(methodes_paiement_discord)
            else:
                methodes_paiement_discord = "Aucun"
        except:
            methodes_paiement_discord = "Aucun"
        
        try:
            amis = requests.get('https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token_discord}).json()
            amis_discord = []
            if amis:
                for ami in amis:
                    donnees = f"{ami['user']['username']}#{ami['user']['discriminator']} ({ami['user']['id']})"
                    if len('\n'.join(amis_discord)) + len(donnees) >= 1024:
                        break
                    amis_discord.append(donnees)
                amis_discord = '\n'.join(amis_discord) if amis_discord else "Aucun"
            else:
                amis_discord = "Aucun"
        except:
            amis_discord = "Aucun"


        try:
            codes_cadeaux = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token_discord}).json()
            codes_cadeaux_discord = []
            if codes_cadeaux:
                for code in codes_cadeaux:
                    nom = code['promotion']['outbound_title']
                    code_cadeau = code['code']
                    donnees = f"Promo -> {nom}\nCode -> {code_cadeau}"
                    if len('\n\n'.join(codes_cadeaux_discord)) + len(donnees) >= 1024:
                        break
                    codes_cadeaux_discord.append(donnees)
                codes_cadeaux_discord = '\n\n'.join(codes_cadeaux_discord) if codes_cadeaux_discord else "Aucun"
            else:
                codes_cadeaux_discord = "Aucun"
        except:
            codes_cadeaux_discord = "Aucun"

    except Exception as e:
        print(f"Erreur lors de la récupération des informations : {e}")
        return

    print(f"""
    Statut                         -> {statut}
    Jeton                          -> {token_discord}
    Nom d'utilisateur              -> {nom_utilisateur_discord}
    Nom d'affichage                -> {nom_affichage_discord}
    Id                             -> {id_utilisateur_discord}
    Créé le                        -> {cree_le_discord}
    Pays                           -> {pays_discord}
    Email                          -> {email_discord}
    Vérifié                        -> {email_verifie_discord}
    Téléphone                      -> {telephone_discord}
    Nitro                          -> {nitro_discord}
    Utilisateurs liés              -> {utilisateurs_lies_discord}
    Décoration d'avatar            -> {decoration_avatar_discord}
    Avatar                         -> {avatar_discord}
    URL de l'avatar                -> {url_avatar_discord}
    Couleur d'accent               -> {couleur_accent_discord}
    Bannière                       -> {bannière_discord}
    Couleur de bannière            -> {couleur_bannière_discord}
    Drapeaux                       -> {drapeaux_discord}
    Drapeaux publics               -> {drapeaux_publics_discord}
    NSFW                           -> {nsfw_discord}
    Authentification multi-facteur -> {mfa_discord}
    Type d'authentificateur        -> {types_authentificateurs_discord}
    Facturation                    -> {methodes_paiement_discord}
    Code cadeau                    -> {codes_cadeaux_discord}
    Guildes                        -> {nombre_guilds}
    Guildes Propriétaire           -> {nombre_guilds_proprietaire}
    {noms_guilds_proprietaire}
    Bio                            -> {bio_discord}
    Amis                           -> {amis_discord}
    """)

def principal():
    token_discord = obtenir_token_discord()
    recuperer_informations_utilisateur(token_discord)

if __name__ == "__main__":
    principal()
