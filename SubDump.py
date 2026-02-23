#!/usr/bin/env python3
"""
SubDump - Subdomain Finder
Modified by KUSH-COD3R
"""

import requests
import json
import time
import sys
import subprocess
import platform


def check_internet():
    """Check internet connection."""
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        subprocess.check_call(['ping', param, '1', 'www.google.com'], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        return True
    except:
        return False


COLORS = {
    'Bl': '\033[30m',
    'Re': '\033[1;31m',
    'Gr': '\033[1;32m',
    'Ye': '\033[1;33m',
    'Blu': '\033[1;34m',
    'Mage': '\033[1;35m',
    'Cy': '\033[1;36m',
    'Wh': '\033[1;37m',
    'reset': '\033[0m'
}


def c(text, color):
    return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"


def autoketik(x):
    """Typing animation."""
    for y in x + "\n":
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(0.030)


def banner():
    print(r""" _______       _            ______                         
|   _   .--.--|  |--.______|   _  \ .--.--.--------.-----.
|   1___|  |  |  _  |______|.  |   \|  |  |        |  _  |
|____   |_____|_____|      |.  |    |_____|__|__|__|   __|
|:  1   |                  |:  1    /              |__|   
|::.. . |                  |::.. . /                      
`-------'                  `------'
        TOOLS  SUBDOMAIN V.1.2   CREDIT © HUNXBYTS         
""")


def find_subdomains(domain):
    """Find subdomains using crt.sh API."""
    subdo_main = []
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                subdomain = entry['name_value']
                if subdomain not in subdo_main:
                    subdo_main.append(subdomain)
    except requests.exceptions.RequestException as e:
        print(f"\n{c('Error:', 'Re')} {c(str(e), 'Re')}")
    except json.JSONDecodeError:
        print(f"\n{c('Error: Invalid response from server', 'Re')}")
    
    return subdo_main


def save_to_file(subdomains, domain):
    """Save subdomains to file."""
    filename = f"subdomains_{domain}_{int(time.time())}.txt"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for subdomain in subdomains:
                f.write(f"{subdomain}\n")
        print(f"\n{c('Results saved to:', 'Gr')} {c(filename, 'Ye')}")
    except Exception as e:
        print(f"\n{c('Error saving file:', 'Re')} {e}")


def main():
    if not check_internet():
        print(c("Error: No internet connection! Please check your network.", "Re"))
        sys.exit(1)
    
    banner()
    
    try:
        domain = input(f"\n\n{c('[ + ]', 'Ye')} {c('ENTER TARGET WEB', 'Wh')} {c('[ex: hacker.com]', 'Ye')} : ")
        
        if not domain.strip():
            print(c("Error: Domain cannot be empty!", "Re"))
            sys.exit(1)
        
        autoketik(f"{c('[ + ]', 'Ye')} {c('SCANNING SUBDOMAIN FOR', 'Wh')} {c(domain, 'Gr')}...")
        time.sleep(2)
        
        subdomains = find_subdomains(domain)
        
        print(f"\n{c('SUBDOMAIN FOUND:', 'Wh')} {c(str(len(subdomains)), 'Gr')}")
        print(c("-" * 40, "Wh"))
        
        for subdomain in subdomains:
            print(subdomain)
        
        if subdomains:
            save = input(f"\n{c('Save results to file?', 'Wh')} {c('Y/N', 'Gr')} : ").lower()
            if save == 'y':
                save_to_file(subdomains, domain)
        
    except KeyboardInterrupt:
        print(f"\n{c('[!] PROGRAM STOPPED...', 'Re')}")
        sys.exit(0)


if __name__ == "__main__":
    main()
