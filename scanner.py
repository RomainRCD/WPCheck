import requests
import json
from bs4 import BeautifulSoup

# URL de base du site à scanner
base_url = "https://www.eap-locations.fr"


# Fonction pour récupérer toutes les URLs du site et les enregistrer dans un fichier JSON
def scan_and_store_site(base_url, output_file="site_pages.json"):
    all_pages = []

    def get_all_links(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            for link in soup.find_all("a"):
                href = link.get("href")
                if href and href.startswith(base_url) and href not in all_pages:
                    all_pages.append(href)
                    print(f"Ajout de la page: {href}")
                    get_all_links(href)
        except requests.RequestException as e:
            print(f"Erreur de requête pour {url}: {e}")

    # Commencez par la page d'accueil
    get_all_links(base_url)

    # Enregistrez toutes les pages dans un fichier JSON
    with open(output_file, "w") as json_file:
        json.dump(all_pages, json_file, indent=4)

    print(f"Pages récupérées : {len(all_pages)}")


# Appeler la fonction pour scanner et stocker le site
scan_and_store_site(base_url)
