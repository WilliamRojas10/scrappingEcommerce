import requests
from bs4 import BeautifulSoup

biblioteca = {
    "tv": "37-tv",
    "monitores": "36-monitores",
    "soportes": "160-soportes",
}

url_lemac = 'https://lezamapc.com.ar'
encabezados = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Diccionario para almacenar los productos por categoría
productos_por_categoria = {clave: [] for clave in biblioteca.keys()}

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

                    # Extraer el título del producto
                    elemento_titulo = producto.find('h2', class_='h3 product-title')
                    titulo = elemento_titulo.text.strip() if elemento_titulo else 'Sin título'

                    # Extraer el precio del producto
                    elemento_precio = producto.find('span', class_='price')
                    precio = elemento_precio.text.strip() if elemento_precio else 'Sin precio'

                    # Agregar el producto a la lista correspondiente
                    productos_por_categoria[clave].append({"titulo": titulo, "precio": precio})

                    # Contador de productos
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

# Mostrar los productos almacenados por categoría
# for categoria, productos in productos_por_categoria.items():
#     print(f"\nProductos en la categoría {categoria}:")
#     for producto in productos:
#         print(f"- {producto['titulo']}: {producto['precio']}")

print(" \n\n\n\n\n\n PEODUCTOS POR CATEGORIA: ",productos_por_categoria["tv"])
