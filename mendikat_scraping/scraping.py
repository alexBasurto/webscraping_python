import requests
from bs4 import BeautifulSoup
import json

# URL base
base_url = "https://www.mendikat.net/com/mount/"

# Número de montes a consultar (por ejemplo, del 1 al 100)
num_montes = 10

data = []

for numero_monte in range(1, num_montes + 1):
    url = base_url + str(numero_monte)
    response = requests.get(url)

    if response.status_code == 200:
        print(f'Extrayendo datos del monte número {numero_monte}...')

        soup = BeautifulSoup(response.text, 'html.parser')

        # Encuentra el div con la clase "section-title"
        section_title_div = soup.find("div", class_="section-title")

        # Extrae el texto del h2 dentro del div
        h2_text = section_title_div.find("h2").text.strip()

        # Separa el texto en nombre del monte y altitud
        nombre_monte, altitud = h2_text.split(" (")
        altitud = altitud[:-1]  # Elimina el paréntesis al final de la altitud

        # Añade la información a la lista de datos.
        data.append({
            "NumeroMonte": numero_monte,
            "NombreMonte": nombre_monte,
            "Altitud": altitud
        })

# Guardar los datos en un archivo JSON
with open('montes.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f'Se han extraído datos de {len(data)} montes y se han guardado en montes.json')
