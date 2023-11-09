Para hacer web scraping del contenido de todos los montes en la página mendikat.net y luego pasarlo a un formato JSON, puedes utilizar Python junto con bibliotecas como Requests y BeautifulSoup para extraer los datos y la biblioteca json para convertirlos a formato JSON. A continuación, te proporciono un ejemplo básico de cómo hacerlo:

Paso 0: Instala PIP:

```bash
sudo apt install python3-pip
```

Paso 0.1: Instala Selenium para poder extraer contenido generado con JS:
```bash
pip install selenium
```
necesario también instalar el controlador de chrome.

Paso 1: Instala las bibliotecas necesarias si aún no las tienes instaladas. Puedes hacerlo a través de pip:

```bash
pip install requests beautifulsoup4
```

Paso 2: A continuación, puedes usar el siguiente código Python para realizar el web scraping y convertir los datos en formato JSON:

```python
import requests
from bs4 import BeautifulSoup
import json

# URL base
base_url = "https://www.mendikat.net/com/mount/"

# Número de montes a consultar (por ejemplo, del 1 al 100)
num_montes = 21225

data = []

for numero_monte in range(1, num_montes + 1):
    url = base_url + str(numero_monte)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraer la información que desees de la página, por ejemplo, el nombre del monte.
        nombre_monte = soup.find("h1", class_="title").text.strip()

        # Añade la información a la lista de datos.
        data.append({
            "NumeroMonte": numero_monte,
            "NombreMonte": nombre_monte
        })

# Guardar los datos en un archivo JSON
with open('montes.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f'Se han extraído datos de {len(data)} montes y se han guardado en montes.json')
```

Asegúrate de ajustar `num_montes` al rango deseado y de expandir la extracción de datos según tus necesidades. El ejemplo anterior solo extrae el nombre del monte y el número de monte, pero puedes agregar más información según lo que necesites. El resultado se guardará en un archivo JSON llamado `montes.json`.



DATOS QUE QUEREMOS EXTRAER:
    - id del monte OK
    - nombre monte cabecera OK
    - altitud OK
    - URL imagen ppal OK
    - URL Mendikat OK
    - nombre
    - otros nombres
    - sierra/macizo
    - altitud
    x datums?? no.... de momento...
    - coordenadas WGS84 (GPS americano) habrá que pasarlas al siguiente formato: 42°58'34.86"N 4°40'26.28"W (quitar espacios, punto por coma...)
    - fecha modificado
    x descripción (pág protegida contra scraping)



