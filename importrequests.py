import requests
import time
import random
import json

# Lire les proxy à partir d'un fichier
with open('proxies.txt', 'r') as f:
    proxies_list = f.readlines()

proxies = [proxy.strip() for proxy in proxies_list]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Origin": "https://www.tiktok.com",
    "Referer": "https://www.tiktok.com/",
    "DNT": "1",
}

# Demander le lien de signalement
url_template = input("Veuillez entrer l'URL de signalement : ")

def send_report(url, headers, proxies):
    response = requests.post(url, headers=headers, proxies={"http": proxies, "https": proxies})
    if response.status_code == 200:
        print("Signalement envoyé")
    else:
        print(f"Échec de l'envoi du signalement, code d'état HTTP : {response.status_code}")

if __name__ == "__main__":
    for _ in range(100):
        random_proxy = random.choice(proxies)
        send_report(url_template, headers, random_proxy)
        time.sleep(random.uniform(1, 1.5))