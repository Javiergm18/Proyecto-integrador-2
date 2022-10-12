from sre_constants import SUCCESS
import requests
from bs4 import BeautifulSoup
from lxml import etree


busqueda = 'play station 5'
busquedaMercadoLibre = busqueda.replace(' ','-')
busquedaMas = busqueda.replace(' ','+')

urlMercadoLibre = 'https://listado.mercadolibre.com.co/' + busquedaMercadoLibre
urlAlkosto = 'https://www.alkosto.com/search/?text='+busquedaMas
urlAlkomprar = 'https://www.alkomprar.com/search/?text=' + busquedaMas
urlKtronix = 'https://www.ktronix.com/search/?text=' + busquedaMas

mercadoLibre = requests.get(urlMercadoLibre)
alkosto = requests.get(urlAlkosto)
alkomprar = requests.get(urlAlkomprar)
ktronix = requests.get(urlKtronix)

# if(mercadoLibre.status_code == 200):
#     soupMercadoLibre = BeautifulSoup(mercadoLibre.content, 'html.parser')
#     titulosMercadoLibre = soupMercadoLibre.find_all('h2', attrs={"class": "ui-search-item__title"})
#     titulosMercadoLibre = [i.text for i in titulosMercadoLibre]
#     urlsMercadoLibre = soupMercadoLibre.find_all('a', attrs={"class": "ui-search-item__group__element shops-custom-secondary-font ui-search-link"})
#     urlsMercadoLibre = [i.get('href') for i in urlsMercadoLibre]
        
#     dom = etree.HTML(str(soupMercadoLibre))
#     preciosMercadoLibre = dom.xpath('//div[@class="ui-search-result__content-wrapper shops-custom-secondary-font"]//div[@class="ui-search-result__content-column ui-search-result__content-column--left"]//div[@class="ui-search-price ui-search-price--size-medium shops__price"]//div[@class="ui-search-price__second-line"]//span[@class="price-tag-fraction"]')
#     preciosMercadoLibre = [i.text.replace(".", "") for i in preciosMercadoLibre]
#     print(titulosMercadoLibre)
#     print(urlsMercadoLibre)
#     print('\n###########################\n')
#     print(preciosMercadoLibre)

if(ktronix.status_code == 200):
    soupKtronix = BeautifulSoup(ktronix.content, 'html.parser')
    dom = etree.HTML(str(soupKtronix))
    titulosKtronix = dom.xpath('//h2[@class="product__information--name"]//a')
    urlsKtronix = titulosKtronix
    titulosKtronix = [i.text for i in titulosKtronix]
    urlsKtronix = ['https://www.ktronix.com' + i.get('href') for i in urlsKtronix]
    preciosKtronix = soupKtronix.find_all('span', attrs={"class": "price"})
    preciosKtronix = [i.text.replace("$", "").replace(".", "") for i in preciosKtronix]
    
    print(titulosKtronix)
    print(urlsKtronix)
    print(len(urlsKtronix))
    print('\n###########################\n')
    print(preciosKtronix)
else:
    print('error')

# if(alkosto.status_code == 200):
#     soupAlkosto = BeautifulSoup(alkosto.content, 'html.parser')
#     dom = etree.HTML(str(soupAlkosto))
#     titulosAlkosto = dom.xpath('//h2[@class="product__information--name"]//a')
#     urlsAlkosto = titulosAlkosto
#     titulosAlkosto = [i.text for i in titulosAlkosto]
#     urlsAlkosto = ['https://www.alkosto.com' + i.get('href') for i in urlsAlkosto]
#     preciosAlkosto = soupAlkosto.find_all('span', attrs={"class": "price"})
#     preciosAlkosto = [i.text.replace("$", "").replace(".", "") for i in preciosAlkosto]
    
#     print(titulosAlkosto)
#     print(urlsAlkosto)
#     print(len(urlsAlkosto))
#     print('\n###########################\n')
#     print(preciosAlkosto)
# else:
#     print('error')

# if(alkomprar.status_code == 200):
#     soupAlkomprar = BeautifulSoup(alkomprar.content, 'html.parser')
#     dom = etree.HTML(str(soupAlkomprar))
#     titulosAlkomprar = dom.xpath('//h2[@class="product__information--name"]//a')
#     urlsAlkomprar = titulosAlkomprar
#     titulosAlkomprar = [i.text for i in titulosAlkomprar]
#     urlsAlkomprar = ['https://www.alkomprar.com' + i.get('href') for i in urlsAlkomprar]
#     preciosAlkomprar = soupAlkomprar.find_all('span', attrs={"class": "price"})
#     preciosAlkomprar = [i.text.replace("$", "").replace(".", "") for i in preciosAlkomprar]

#     print(titulosAlkomprar)
#     print(urlsAlkomprar)
#     print(len(urlsAlkomprar))
#     print('\n###########################\n')
#     print(preciosAlkomprar)
# else:
#     print('error')