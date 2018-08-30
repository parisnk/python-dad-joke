import requests
from colorama import init, Fore, Back

init()

response = requests.get(
    'https://icanhazdadjoke.com/',
    headers = {'Accept':'application/json'})

print(Back.BLUE + Fore.YELLOW + ' your dad joke: {0}'.format(response.json()['joke']))

input("press ENTER to continue")

