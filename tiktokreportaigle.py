import requests
import time
import random
import json
from datetime import datetime

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

# Demander l'URL de signalement
url_template = input("Veuillez entrer l'URL de signalement : ")

def send_report(url, headers, proxies):
    proxy = random.choice(proxies)
    proxy_agent = requests.get(f"http://{proxy}").text
    try:
        response = requests.post(url, headers=headers, proxies={"http": proxy_agent, "https": proxy_agent}, timeout=5)
        if response.status_code == 200:
            print(f"           {datetime.now().strftime('%H:%M:%S')}  ", end="")
            print("Succès : signalement envoyé")
        else:
            print(f"           {datetime.now().strftime('%H:%M:%S')}  ", end="")
            print(f"Échec de l'envoi du signalement, code d'état HTTP : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"           {datetime.now().strftime('%H:%M:%S')}  ", end="")
        print(f"Échec de la requête : {e}")
    finally:
        time.sleep(0.5)

if __name__ == "__main__":
    report_count = 0
    report_count_total = 0

    while True:
        proxy = random.choice(proxies)
        proxy_agent = requests.get(f"http://{proxy}").text
        for _ in range(2):
            send_report(url_template, headers, proxies)
            report_count += 1
            report_count_total += 1
        print(f"           {datetime.now().strftime('%H:%M:%S')}  ", end="")
        print(f"Moyenne de {report_count_total} signalements/seconde")
        report_count_total = 0