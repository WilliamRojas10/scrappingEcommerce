from urllib.request import urlopen 
from bs4 import BeautifulSoup

def bajar(laDir): 
   laPag = urlopen(laDir) 
   return BeautifulSoup(laPag.read(),features="html.parser")

pagina= bajar("https://lezamapc.com.ar/36-monitores")
print(pagina.prettify())