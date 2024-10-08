import requests
from bs4 import BeautifulSoup

# URL de la página donde buscar productos
url = 'https://electropc.com.ar/'

# Configurar los headers para evitar ser bloqueado
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Realizar la solicitud HTTP a la página
response = requests.get(url, headers=headers)

# Si la solicitud fue exitosa
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extraer el nombre del producto
    nombre = soup.find('h1', class_='w-post-elm post_title us_custom_8e46ea77 entry-title color_link_inherit').text.strip()
    
    # Extraer el precio contado
    precio_contado = soup.find('span', class_='woocommerce-Price-amount amount').text.strip()

    # Extraer el precio de lista
    precio_lista = soup.find('h5').find('strong').text.strip()

    # Extraer las categorías
    categorias = soup.find('div', class_='w-post-elm-list')
    lista_categorias = [cat.text.strip() for cat in categorias.find_all('span', class_='w-btn-label')]

    # Extraer la descripción
    descripcion = soup.find('div', class_='w-post-elm post_content us_custom_5426a972').find('p').text.strip()

    # Extraer el SKU
    sku = soup.find('div', class_='w-post-elm product_field sku us_custom_d8c12f47 has_text_color product_meta').find('span', class_='sku').text.strip()

    # Extraer la disponibilidad
    disponibilidad = soup.find('span', class_='ac-backorders-productpage').text.strip()

    # Imprimir los resultados
    print(f"Nombre: {nombre}")
    print(f"Precio Contado: {precio_contado}")
    print(f"Precio Lista: {precio_lista}")
    print(f"Categorías: {', '.join(lista_categorias)}")
    print(f"Descripción: {descripcion}")
    print(f"SKU: {sku}")
    print(f"Disponibilidad: {disponibilidad}")
else:
    print(f"Error al acceder a la página: {response.status_code}")
