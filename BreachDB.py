#!/usr/bin/env python3
# BreachDB.py: Query the Rapid7 breach database for email addressess and passwords.
# Author: Jessi
# Usage: ./BreachDB.py -d <domain.com> -o <output-file> -l <results-limit>


import requests
import sys
import argparse
import time
import json
from collections import Counter
from colorama import Fore, Style


# Define colorama colors.
GREEN = Fore.GREEN
RED = Fore.RED
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
PINK = Fore.MAGENTA
BRIGHT = Style.BRIGHT
DIM = Style.DIM
NORM = Style.NORMAL
RST = Style.RESET_ALL


# Error if no arguments and print example.
if len(sys.argv) <= 1:
    print(f'{RED}{BRIGHT}Rapid7 Breach Database{RST}: Query the Rapid7 breach database for email addresses and passwords.{RST}\n')
    print(f'{RED}{BRIGHT}Error{DIM}: -d (--domain) REQUIRED{RST}')
    print(f'{PINK}{BRIGHT}Example:{RED} breachDB.py{NORM}{WHITE} -d domain.com -o domain.com_unpw.txt{RST}\n')
    print(f'{DIM}-h (--help) to see full usage and arguments.{RST}')
    print('\n')


# Define parser and arguments.
parser = argparse.ArgumentParser(description=f'{RED}{BRIGHT}Rapid7 Breach Database{RST}: Query the Rapid7 breach database for email addresses and passwords.{RST}')

parser.add_argument('-d', '--domain', help=f'Target domain {RED}{BRIGHT}REQUIRED{RST}', default=None, required=True)
parser.add_argument('-o', '--output', help=f'Output file name {DIM}OPTIONAL (Defualt: results.txt){RST}', default='results.txt', required=False)
parser.add_argument('-l', '--limit', help=f"Limit results {DIM} OPTIONAL (Default: 1000){RST}", type=int, default=1000, required=False)
parser.add_argument('-a', '--apikey', help=f'API Key {DIM}OPTIONAL (Default: R7 default api key.){RST}', default='PUT-API-KEY-HERE', required=False)

args = parser.parse_args()


# Set variables.
domain = args.domain
output = args.output
apikey = args.apikey
limit = args.limit
apiurl = 'https://pwnd.tiden.io/search'
headers = {"User-Agent": "Mozilla/5.0", "Authorization": "apikey {}".format(apikey)}
params = {"domain": domain, "limit": limit}


# Get results.
print(f'{PINK}{BRIGHT}[*] {NORM}{WHITE}Querying: {DIM}pwnd.tiden.io{RST}')
print(f'{PINK}{BRIGHT}[*] {NORM}{WHITE}Domain: {DIM}{domain}{RST}')
print(f'{PINK}{BRIGHT}[*] {NORM}{WHITE}Results limit: {DIM}{limit}{RST}')
time.sleep(2)

r = requests.get(apiurl, headers=headers, params=params)
data = r.json()


# Count results and print.
results = 0
for d in data:
    results += 1
print(f"{BRIGHT}{GREEN}[+] {RST}Found {WHITE}{results}{RST} entries for {WHITE}{domain}{RST}")


# Get usernames and passwords from results.
results_table = []
password_table = []

for entry in data:
    username = []
    password = []
    username.append(entry["username"])
    password.append(entry["password"])
    results_table.append(f'{username}:{password}')
    password_table.append("".join(password))

common_passwords = Counter(password_table).most_common(3)
commonpw_table = ["%i. %s" % (index + 1, value) for index, value in enumerate(common_passwords)]
finalpw_table = "\n".join(commonpw_table)

final_table = ",".join(results_table).replace("[","").replace("]","").replace(",","\n").replace("'","") # Format final table.


# Write results table to file.
with open(output,"wt") as results_file:
    results_file.write(final_table)

print(f"{BRIGHT}{GREEN}[+] {RST}Wrote results to {WHITE}{output}{RST}")
print(f'{PINK}{BRIGHT}[*] {NORM}{WHITE}Top 3 Passwords{RST}')
print(finalpw_table.replace("(","").replace(")","").replace(","," :").replace("'",""))
