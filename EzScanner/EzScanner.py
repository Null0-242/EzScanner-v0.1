import os, socket, platform, subprocess, requests
from colorama import Fore, Style, init
init(autoreset=True)

# Colori personalizzati
USER_COLOR = Fore.LIGHTGREEN_EX
DOLLAR_COLOR = Fore.GREEN
WHITE = Fore.WHITE
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    ascii_logo = """
 ██████████             █████████                                                             
░░███░░░░░█            ███░░░░░███                                                            
 ░███  █ ░   █████████░███    ░░░   ██████   ██████   ████████   ████████    ██████  ████████ 
 ░██████    ░█░░░░███ ░░█████████  ███░░███ ░░░░░███ ░░███░░███ ░░███░░███  ███░░███░░███░░███
 ░███░░█    ░   ███░   ░░░░░░░░███░███ ░░░   ███████  ░███ ░███  ░███ ░███ ░███████  ░███ ░░░ 
 ░███ ░   █   ███░   █ ███    ░███░███  ███ ███░░███  ░███ ░███  ░███ ░███ ░███░░░   ░███     
 ██████████  █████████░░█████████ ░░██████ ░░████████ ████ █████ ████ █████░░██████  █████    
░░░░░░░░░░  ░░░░░░░░░  ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░      v0.1
"""
    print(GREEN + ascii_logo + RESET)

def prompt():
    return USER_COLOR + "user" + DOLLAR_COLOR + "$ " + WHITE + "-} " + RESET

def scan_ip(ip):
    print(f"{WHITE}🔍 Scanning IP: {YELLOW}{ip}{RESET}\n")

    try:
        info = requests.get(f'https://ipinfo.io/{ip}/json').json()
        print(f"{WHITE}IP Address:{RESET} {info.get('ip','N/A')}")
        print(f"{WHITE}Hostname:{RESET} {info.get('hostname','N/A')}")
        print(f"{WHITE}City:{RESET} {info.get('city','N/A')}")
        print(f"{WHITE}Region:{RESET} {info.get('region','N/A')}")
        print(f"{WHITE}Country:{RESET} {info.get('country','N/A')}")
        print(f"{WHITE}Location (Lat,Lon):{RESET} {info.get('loc','N/A')}")
        print(f"{WHITE}Postal Code:{RESET} {info.get('postal','N/A')}")
        print(f"{WHITE}Timezone:{RESET} {info.get('timezone','N/A')}")
        print(f"{WHITE}Organization / ISP:{RESET} {info.get('org','N/A')}")
        print(f"{WHITE}ASN:{RESET} {info.get('asn','N/A')}")
    except:
        print(f"{RED}Failed to retrieve IP info{RESET}")

    try:
        hostname = socket.gethostbyaddr(ip)[0]
        print(f"{WHITE}DNS Hostname:{RESET} {hostname}")
    except:
        print(f"{RED}DNS lookup failed{RESET}")

    param = '-n' if platform.system().lower() == 'windows' else '-c'
    try:
        print(f"\n{WHITE}📶 Ping Test:{RESET}")
        output = subprocess.check_output(['ping', param, '15', ip], universal_newlines=True)
        print(YELLOW + output + RESET)
    except:
        print(f"{RED}Ping failed{RESET}")

def main():
    clear()
    logo()
    print()
    print(f"{WHITE}powered By {DOLLAR_COLOR}Null0\n")
    print(f"{WHITE}Options:")
    print(f"{WHITE}1:{GREEN} Scan IP connection (IP info, DNS, ping){RESET}")
    print(f"{WHITE}0:{GREEN} Exit{RESET}\n")

    while True:
        choice = input(prompt())
        if choice == '1':
            ip = input(f"{WHITE}Enter IP to scan:{RESET} ")
            clear()
            logo()
            scan_ip(ip)
            print()
        elif choice == '0':
            print(f"{YELLOW}Exiting...{RESET}")
            break
        else:
            print(f"{RED}Invalid option.{RESET}")

if __name__ == "__main__":
    main()
