import random
import requests
from proxyscrape import create_collector, ProxyType

# Liste des proxies
collector = create_collector(proxy_type=ProxyType.HTTP, max_try=2, randomize=True)
proxies = collector.get_proxies()

# Compte TikTok cible
compte_tiktok = "COMPTE_TIKTOK"

# Lien de signalement
lien_signalement = "LIEN_SIGNALEMENT"

# Nombre de signalements à envoyer
nombre_signalements = 10

for _ in range(nombre_signalements):
    # Sélectionner un proxy aléatoire
    proxy = random.choice(proxies)

    # Envoyer le signalement
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    }
    data = {
        'content': f'spam\n\n#tiktok #spam #report #automated',
        'entity_type': 'video',
        'entity_id': f'video-{compte_tiktok}',
        'reason': 'Hate speech or bullying',
        'submit': 'Signaler'
    }
    try:
        response = requests.post(lien_signalement, headers=headers, data=data, proxies={'http': proxy, 'https': proxy})
        print(f"Signalement envoyé avec le proxy {proxy}")
    except Exception as e:
        print(f"Échec de l'envoi du signalement avec le proxy {proxy}: {e}")