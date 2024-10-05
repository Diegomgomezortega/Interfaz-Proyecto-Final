from urllib.request import urlopen 
from bs4 import BeautifulSoup

def bajar(laDir): 
   laPag = urlopen(laDir) 
   return BeautifulSoup(laPag.read(),features="html.parser")

pagina= bajar("https://lezamapc.com.ar/114-micro-amd")

paginacion = pagina.find('nav', class_='pagination')

if paginacion:
    # Encontrar el elemento <ul> dentro del <nav>
    ul_paginacion = pagina.find('ul', class_='page-list clearfix text-sm-center')

    if ul_paginacion:
        # Encontrar todos los elementos 'li' dentro del <ul>
        paginas = ul_paginacion.find_all('li')

        if len(paginas) > 1:
            # Obtener el penúltimo elemento 'li'
            penultimo_li = paginas[-2]

            # Extraer el número de páginas desde el texto del enlace dentro del penúltimo 'li'
            max_paginas = penultimo_li.find('a').text.strip()

            print(f"El número máximo de páginas es: {max_paginas}")
        else:
            print("No se encontró el penúltimo elemento 'li' en la paginación.")
    else:
        print("No se encontró el elemento <ul> dentro de <nav>.")
else:
    print("No se encontró el elemento <nav> con la clase 'pagination'.")

# Obtener una lista de todas las etiquetas 'article' en la página
articles = pagina.find_all('article')

# Imprimir los enlaces encontrados
for article in articles:
    print(article)

# print(pagina.prettify())