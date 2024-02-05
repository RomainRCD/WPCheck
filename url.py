import requests
import json
import random
import time
import datetime  # Ajoutez cette ligne pour travailler avec les dates

# Charger la liste des pages depuis le fichier JSON
with open("site_pages.json", "r") as json_file:
    pages = json.load(json_file)


# Fonction pour vérifier les URLs
def check_urls(pages):
    errors = []  # Une liste pour stocker les URLs avec des erreurs

    for url in pages:
        try:
            response = requests.get(url)
            status_code = response.status_code
            if status_code != 200:
                print(f"Erreur détectée! URL: {url} - Status Code: {status_code}")
                errors.append((url, status_code))
            else:
                print(f"URL OK: {url}")
        except requests.RequestException as e:
            print(f"Erreur de requête pour {url}: {e}")
        time.sleep(15)  # Attendez 15 secondes avant la prochaine vérification

    # Créez un rapport avec la date
    now = datetime.datetime.now()
    report_filename = f"rapport_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    with open(report_filename, "w") as report_file:
        report_file.write("Rapport de Vérification d'URLs\n")
        report_file.write(f"Date et Heure: {now}\n\n")

        if errors:
            report_file.write("URLs avec Erreurs:\n")
            for url, status_code in errors:
                report_file.write(f"URL: {url} - Status Code: {status_code}\n")
        else:
            report_file.write("Aucune Erreur Détectée\n")


# Appeler la fonction pour vérifier les URLs
check_urls(pages)
