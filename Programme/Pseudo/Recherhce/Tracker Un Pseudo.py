import requests
import re
import bs4

from colorama import Fore, Back, Style, init
import os

os.system('color 4')

menu = r"""                                                                                           
                                  ...:----:...                                              
                             .:=#@@@@@@@@@@@@@@%*-..                                        
                          .:#@@@@@@@%#*****#%@@@@@@@+..                                     
                       ..-@@@@@%-...... ........+@@@@@@..                                   
                       :%@@@@=..   .#@@@@@@@@#=....+@@@@*.                                  
                     .+@@@@=.      .*@@@%@@@@@@@@=...*@@@@:.                                
                    .#@@@%.                 .=@@@@@=. .@@@@-.                               
                   .=@@@#.                    .:%@@@*. -@@@%:.                              
                   .%@@@-                       .*@@*. .+@@@=.                              
                   :@@@#.                              .-@@@#.                              
                   -@@@#                                :%@@@.                              
                   :@@@#.                              .-@@@#.                              
                   .%@@@-.                             .+@@@=.                              
                   .+@@@#.                             -@@@%:.                              
                   .*@@@%.                          .:@@@@-.                               
                     .+@@@@=..                     ..*@@@@:.                                
                       :%@@@@-..                ...+@@@@*.                                  
                       ..-@@@@@%=...         ...*@@@@@@@@#.                                 
                          .:*@@@@@@@%*++++**@@@@@@@@=:*@@@@#:.                              
                             ..=%@@@@@@@@@@@@@@%#-.   ..*@@@@%:.                            
                                .....:::::::....       ...+@@@@%:                           
                                                          ..+@@@@%-.                        
                                                            ..=@@@@%-.                      
                                                              ..=@@@@@=.                    
                                                                .=%@@@@=.                  
                                                                  ..-%@@@-.                 
                                                                     ....                 
                                ╔═══════════════════╗
                                ║ Tracker Un Pseudo ║
                                ╚═══════════════════╝          
"""

print(menu)

sites = {
        "Roblox Trade": "https://rblx.trade/p/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Instagram": "https://www.instagram.com/{}",
        "Paypal": "https://www.paypal.com/paypalme/{}",
        "GitHub": "https://github.com/{}",
        "Giters": "https://giters.com/{}",
        "Pinterest": "https://www.pinterest.com/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "Telegram": "https://t.me/{}",
        "Steam": "https://steamcommunity.com/id/{}",
        "Blogger": "https://{}.blogspot.com",
        "Tumblr": "https://{}.tumblr.com",
        "SoundCloud": "https://soundcloud.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "About.me": "https://about.me/{}",
        "Flickr": "https://www.flickr.com/people/{}",
        "Keybase": "https://keybase.io/{}",
        "Last.fm": "https://www.last.fm/user/{}",
        "Slideshare": "https://www.slideshare.net/{}",
        "Behance": "https://www.behance.net/{}",
        "Quora": "https://www.quora.com/profile/{}",
        "Patreon": "https://www.patreon.com/{}",
        "Myspace": "https://myspace.com/{}",
        "Kaggle": "https://www.kaggle.com/{}",
        "Periscope": "https://www.pscp.tv/{}",
        "Disqus": "https://disqus.com/by/{}",
        "Mastodon": "https://mastodon.social/@{}",
        "GitLab": "https://gitlab.com/{}",
        "Giphy": "https://giphy.com/{}",
        "LiveJournal": "https://{}.livejournal.com",
        "CodeWars": "https://www.codewars.com/users/{}",
        "Gumroad": "https://gumroad.com/{}",
        "Spotify": "https://open.spotify.com/user/{}",
        "Weebly": "https://{}.weebly.com",
        "YouTube": "https://www.youtube.com/{}",
        "ProductHunt": "https://www.producthunt.com/@{}",
        "Mix": "https://mix.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "Strava": "https://www.strava.com/athletes/{}",


        "Internet Archive": "https://archive.org/search?query={}",
        "Twitter Archive": "https://web.archive.org/web/*/https://twitter.com/{}/status/*",
        "Linktree": "https://linktr.ee/{}",
        "Xbox": "https://www.xboxgamertag.com/search/{}",
        "Twitter": "https://twitter.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "Goodreads": "https://www.goodreads.com/{}",
        "VK": "https://vk.com/{}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{}",
        "Dribbble": "https://dribbble.com/{}",
        "AngelList": "https://angel.co/{}",
        "500px": "https://500px.com/{}",
        "LinkedIn": "https://www.linkedin.com/in/{}",
        "WhatsApp": "https://wa.me/{}",
        "Discord": "https://discord.com/users/{}",
        "Weibo": "https://weibo.com/{}",
        "OKCupid": "https://www.okcupid.com/profile/{}",
        "Meetup": "https://www.meetup.com/members/{}",
        "CodePen": "https://codepen.io/{}",
        "StackOverflow": "https://stackoverflow.com/users/{}",
        "HackerRank": "https://www.hackerrank.com/{}",
        "Xing": "https://www.xing.com/profile/{}",
        "Deezer": "https://www.deezer.com/en/user/{}",
        "Snapfish": "https://www.snapfish.com/{}",
        "Tidal": "https://tidal.com/{}",
        "Dailymotion": "https://www.dailymotion.com/{}",
        "Ravelry": "https://www.ravelry.com/people/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Vine": "https://vine.co/u/{}",
        "Foursquare": "https://foursquare.com/user/{}",  
        "Ello": "https://ello.co/{}",
        "Hootsuite": "https://hootsuite.com/{}",
        "Prezi": "https://prezi.com/{}",
        "Groupon": "https://www.groupon.com/profile/{}",
        "Liveleak": "https://www.liveleak.com/c/{}",
        "Joomla": "https://www.joomla.org/user/{}",
        "StackExchange": "https://stackexchange.com/users/{}",
        "Taringa": "https://www.taringa.net/{}",
        "Shopify": "https://{}.myshopify.com",
        "8tracks": "https://8tracks.com/{}",
        "Couchsurfing": "https://www.couchsurfing.com/people/{}",
        "OpenSea": "https://opensea.io/{}",
        "Trello": "https://trello.com/{}",
        "Fiverr": "https://www.fiverr.com/{}",
        "Badoo": "https://badoo.com/profile/{}",
        "Rumble": "https://rumble.com/user/{}",
        "Wix": "https://www.wix.com/website/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Gumroad": "https://gumroad.com/{}",
        "Dailymotion": "https://www.dailymotion.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{}",
        "Snapfish": "https://www.snapfish.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "VK": "https://vk.com/{}",
}


def site_exception(nom_utilisateur, site, contenu_page):
    if site == "Paypal":
        contenu_page = contenu_page.replace(f'slug_name={nom_utilisateur}', '')
    elif site == "TikTok":
        contenu_page = contenu_page.replace(f'\\u002f@{nom_utilisateur}"', '')
    return contenu_page

nombre_sites = 0
nombre_trouves = 0
sites_et_urls_trouves = []

nom_utilisateur = input("Nom d'utilisateur à scanner : ").lower()

print("Analyse en cours...")

for site, modele_url in sites.items():
    try:
        nombre_sites += 1
        url = modele_url.format(nom_utilisateur)
        try:
            reponse = requests.get(url, timeout=5)
            if reponse.status_code == 200:
                contenu_page = re.sub(r'<[^>]*>', '', reponse.text.lower().replace(url, "").replace(f"/{nom_utilisateur}", ""))
                contenu_page = site_exception(nom_utilisateur, site, contenu_page)
                texte_page = bs4.BeautifulSoup(reponse.text, 'html.parser').get_text().lower().replace(url, "")
                
                titre_page = bs4.BeautifulSoup(reponse.content, 'html.parser').title
                titre_page = titre_page.string.lower() if titre_page and titre_page.string else ""

                trouve = False
                if nom_utilisateur in titre_page or nom_utilisateur in contenu_page or nom_utilisateur in texte_page:
                    nombre_trouves += 1
                    sites_et_urls_trouves.append(f"{site}: {url}")
                    trouve = True
                
                if trouve:
                    print(f"Nom d'utilisateur trouvé sur {site} : {url}")
                else:
                    print(f"Nom d'utilisateur non trouvé sur {site}")

        except requests.exceptions.Timeout:
            print(f"Le site {site} a pris trop de temps à répondre.")
        except requests.exceptions.ConnectionError:
            print(f"Erreur de connexion lors de l'accès à {site}.")
        except Exception as e:
            print(f"Erreur lors de l'accès à {site} : {e}")
    except:
        pass

print(f"\nTotal de sites vérifiés : {nombre_sites}")
print(f"Total de sites trouvés : {nombre_trouves}")

for site_et_url_trouve in sites_et_urls_trouves:
    print(f"Site trouvé : {site_et_url_trouve}")