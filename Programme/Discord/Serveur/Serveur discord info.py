import requests

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
                                              
                                             ╔═══════════════════════╗
                                             ║ Serveur Discord Info  ║
                                             ╚═══════════════════════╝     
"""

print(menu)

def ErrorModule(e):
    print(f"Module error: {e}")

def ErrorUrl():
    print("URL error")

def Error(e):
    print(f"Error: {e}")

def Continue():
    input("Press Enter to continue...")

def Reset():
    pass

try:
    invite = input("Server Invitation -> ")
    
    try:
        invite_code = invite.split("/")[-1]
    except Exception as e:
        print(f"Error parsing invite code: {e}")
        invite_code = invite

    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

    if response.status_code == 200:
        api = response.json()

        type_value = api.get('type', "None")
        code_value = api.get('code', "None")
        inviter_info = api.get('inviter', {})
        inviter_id = inviter_info.get('id', "None")
        inviter_username = inviter_info.get('username', "None")
        inviter_avatar = inviter_info.get('avatar', "None")
        inviter_discriminator = inviter_info.get('discriminator', "None")
        inviter_public_flags = inviter_info.get('public_flags', "None")
        inviter_flags = inviter_info.get('flags', "None")
        inviter_banner = inviter_info.get('banner', "None")
        inviter_accent_color = inviter_info.get('accent_color', "None")
        inviter_global_name = inviter_info.get('global_name', "None")
        inviter_banner_color = inviter_info.get('banner_color', "None")
        expires_at = api.get('expires_at', "None")
        flags = api.get('flags', "None")
        server_info = api.get('guild', {})
        server_id = server_info.get('id', "None")
        server_name = server_info.get('name', "None")
        server_icon = server_info.get('icon', "None")
        server_features = server_info.get('features', [])
        server_features = ' / '.join(server_features) if server_features else "None"
        server_verification_level = server_info.get('verification_level', "None")
        server_nsfw_level = server_info.get('nsfw_level', "None")
        server_description = server_info.get('description', "None")
        server_nsfw = server_info.get('nsfw', "None")
        server_premium_subscription_count = server_info.get('premium_subscription_count', "None")
        channel_info = api.get('channel', {})
        channel_id = channel_info.get('id', "None")
        channel_type = channel_info.get('type', "None")
        channel_name = channel_info.get('name', "None")
    else:
        ErrorUrl()

    print(f"""
    Invitation Information:
    Invitation         : {invite}
    Type               : {type_value}
    Code               : {code_value}
    Expired            : {expires_at}
    Server ID          : {server_id}
    Server Name        : {server_name}
    Channel ID         : {channel_id}
    Channel Name       : {channel_name}
    Channel Type       : {channel_type}
    Server Description : {server_description}
    Server Icon        : {server_icon}
    Server Features    : {server_features}
    Server NSFW Level  : {server_nsfw_level}
    Server NSFW        : {server_nsfw}
    Flags              : {flags}
    Server Verification Level : {server_verification_level}
    Server Premium Subscription Count : {server_premium_subscription_count}
    """)

    if inviter_info:
        print(f"""
        Inviter Information:
        ID            : {inviter_id}
        Username      : {inviter_username}
        Global Name   : {inviter_global_name}
        Avatar        : {inviter_avatar}
        Discriminator : {inviter_discriminator}
        Public Flags  : {inviter_public_flags}
        Flags         : {inviter_flags}
        Banner        : {inviter_banner}
        Accent Color  : {inviter_accent_color}
        Banner Color  : {inviter_banner_color}
        """)

    Continue()
    Reset()
except Exception as e:
    Error(e)
