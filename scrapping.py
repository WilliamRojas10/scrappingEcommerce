import requests
from bs4 import BeautifulSoup

biblioteca = { "tv":"37-tv", 
               "monitores": "36-monitores", 
               "soportes":"160-soportes",
               "electroPC": 'https://electropc.com.ar/categoria'
            }

# biblioteca = { "tv":["37-tv", "monitores-de-oficina", "monitores-gamer"],
#                "monitores": ["36-monitores"], "soportes":"160-soportes"}

# URL  de la página que quieres scrapear
url_lemac = f'https://lezamapc.com.ar'
url_electroPco = f'https://electropc.com.ar/categoria'

# 'https://electropc.com.ar/categoria/monitores/monitores-gamer/page/2/'
# 'https://electropc.com.ar/categoria/monitores/monitores-de-oficina/'
# 'https://electropc.com.ar/categoria/monitores/monitores-diseño-monitores/'
# 'https://electropc.com.ar/categoria/impresoras/'
# 'https://electropc.com.ar/categoria/perifericos/teclados-gamer-teclados/'
# 'https://electropc.com.ar/categoria/perifericos/mouse/mouse-gamer-mouse/'
# 'https://electropc.com.ar/categoria/perifericos/mouse-pad/'
# 'https://electropc.com.ar/categoria/notebooks/notebooks-gamer-notebooks/'
# 'https://electropc.com.ar/categoria/notebooks/notebooks-de-oficina-notebooks/'
# 'https://electropc.com.ar/categoria/conectividad/routers-conectividad/'
# 'https://electropc.com.ar/categoria/conectividad/placas-de-red-wifi-conectividad-conectividad/'
# 'https://electropc.com.ar/categoria/sillas-gamers/sillas-gamer-sillas-gamer/'
# 'https://electropc.com.ar/pc-oficina/'
# 'https://electropc.com.ar/categoria/fuentes/certificadas-fuentes/'
# 'https://electropc.com.ar/categoria/fuentes/gen%c3%a9ricas-fuentes/'

# Definir encabezados con un user-agent de un navegador real
encabezados = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def obtener_productos_lemac (url):
    pass

def obtener_productos_electropc (url):
    pass


def buscar_productos (nombre):
    pass

lista =  []

# Variable para controlar la paginación
for clave, valor in biblioteca.items():
    print(f"\n\n-------------Buscando {clave} en la biblioteca----------------")
    numero_pagina = 1
    contador = 0

    while True:

    # Construir la URL de la página actual
        url = f'{url_lemac}/{valor}?page={numero_pagina}'
    
        try:
            # Realizar la petición HTTP
            respuesta = requests.get(url, headers=encabezados)

            # Verificar si la solicitud fue exitosa
            if respuesta.status_code == 200:
                print(f"Accediendo a la página : {url}")

                # Parsear el contenido de la página con BeautifulSoup
                sopa = BeautifulSoup(respuesta.content, 'html.parser')

                # Inicializar un indicador de productos encontrados
                productos_encontrados = False

                # Buscar todos los productos en la página
                for producto in sopa.find_all('div', class_='product-description'):
                    productos_encontrados = True  # Se encontraron productos
                    #if buscado in producto:
                        #listaEncontrado = lista.append(producto)
                    # Extraer el título del producto
                    elemento_titulo = producto.find('h2', class_='h3 product-title')
                    titulo = elemento_titulo.text.strip() if elemento_titulo else 'Sin título'

                    # Extraer el precio del producto
                    elemento_precio = producto.find('span', class_='price')
                    precio = elemento_precio.text.strip() if elemento_precio else 'Sin precio'

                    # Imprimir la información del producto
                    contador += 1
                    print(f"{contador}_ Producto: {titulo}, Precio: {precio}")
            
                # Si no se encontraron productos, salir del bucle
                if not productos_encontrados:
                    print("No se encontraron más productos en esta página.")
                    break

                

                # Incrementar el número de página para la siguiente iteración
                numero_pagina += 1
           
            else:
                # Si no fue exitosa, imprimir el código de error
                print(f"Error al acceder a la página. Código de estado: {respuesta.status_code}")
                break

        except Exception as e:
            print(f"Se produjo un error al intentar acceder a la página: {str(e)}")
            break

    print(f"Se encontraron {contador} productos en la biblioteca {clave}.")