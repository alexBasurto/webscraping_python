from selenium import webdriver

# Inicializa el controlador de Selenium (asegúrate de tener el controlador correspondiente instalado)
# En este ejemplo, se utiliza el controlador de Chrome.
driver = webdriver.Chrome(executable_path="ruta_del_controlador_chrome")

# URL de la página web
url = "https://www.mendikat.net/com/mount/8377"

# Accede a la página web
driver.get(url)

# Espera un tiempo para que la página cargue completamente (ajusta según sea necesario)
driver.implicitly_wait(10)

# Encuentra el elemento <input> por su ID
input_element = driver.find_element_by_id("mountain.position.utm")

# Obtiene el valor del atributo "value" que contiene las coordenadas
coordenadas = input_element.get_attribute("value")

print(f"Coordenadas UTM: {coordenadas}")

# Cierra el controlador de Selenium
driver.quit()
