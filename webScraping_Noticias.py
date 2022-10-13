# from sre_constants import SUCCESS
import requests
from bs4 import BeautifulSoup
from lxml import etree
from pymongo import MongoClient
import datetime

fecha = str(datetime.date.today())

mongoHost = 'mongodb://localhost'
client = MongoClient(mongoHost)

db = client['integrador2']
collection = db['noticias']

# urlElTiempo = 'https://www.eltiempo.com/'
elTiempo = requests.get('https://www.eltiempo.com/')

# urlPulzo = 'https://www.pulzo.com/'
pulzo = requests.get('https://www.pulzo.com/')

# urlElColombiano = 'https://www.elcolombiano.com/'
elColombiano = requests.get('https://www.elcolombiano.com/')

# urlElHeraldo = 'https://www.elheraldo.co/'
elHeraldo = requests.get('https://www.elheraldo.co/')

allNoticias = []

# El Tiempo Ya funciona
if(elTiempo.status_code == 200):
    soup = BeautifulSoup(elTiempo.content, 'html.parser')
    dom = etree.HTML(str(soup))
    titulos = dom.xpath('//article[@class="image-left"]//h2[@class="title-container"]//a[2]')
    imagenes = dom.xpath('//article[@class="image-left"]//div[@class="recurso"]//figure[@class="image-container"]//a[@class="image page-link"]//meta[@itemprop="url"]')
    imagenes = [i.get('content') for i in imagenes]
    urls = dom.xpath('//article[@class="image-left"]//h2[@class="title-container"]//a[1]')
    urls = ['https://www.eltiempo.com'+i.get('href') for i in urls]
    titulos = [i.text for i in titulos]
    categorias = dom.xpath('//article[@class="image-left"]//div[@class="article-details"]//div[@class="category-published"]//a')
    categorias = [i.text for i in categorias]
    for i in range(len(imagenes)):
        collection.insert_one({"imagen": imagenes[i], "titulo": titulos[i], "url": urls[i],"categoria": categorias[i], "fecha": fecha, "fuente": "El Tiempo"})
        allNoticias.append([imagenes[i], titulos[i], urls[i], categorias[i]])
    
# Pulzo Ya funciona
if(pulzo.status_code == 200):
    soup = BeautifulSoup(pulzo.content, 'html.parser')
    dom = etree.HTML(str(soup))
    titulos = dom.xpath('//div[@class="container-texts"]//a[2]//h2[@class="title-container text-article"]')
    imagenes = dom.xpath('//div[@class="section-image-category"]//img[@class="image-article"]')
    imagenes = [i.get('srcset').split(',')[0] for i in imagenes]
    urls = dom.xpath('//div[@class="container-texts"]//a[2]')
    urls = ['https://www.pulzo.com/' + i.get('href') for i in urls]
    titulos = [i.text for i in titulos]
    categorias = dom.xpath('//div[@class="container-texts"]//h3[@class="title-container text-new-category category-published"]')
    categorias = [i.text[2:-1] for i in categorias]
    for i in range(len(imagenes)):
        collection.insert_one({"imagen": imagenes[i], "titulo": titulos[i], "url": urls[i],"categoria": categorias[i], "fecha": fecha, "fuente": "Pulzo"})
        allNoticias.append([imagenes[i], titulos[i], urls[i], categorias[i]])

# El Colombiano Ya funciona
if(elColombiano.status_code == 200):
    soup = BeautifulSoup(elColombiano.content, 'html.parser')
    dom = etree.HTML(str(soup))
    titulos = dom.xpath('//div[@class="noticia-segundaria"]//span[@class="priority-content"]')
    imagenes = dom.xpath('//div[@class="noticia-segundaria"]//div[@class="left"]//a//img')
    imagenes = [i.get('src') for i in imagenes]
    urls = dom.xpath('//div[@class="noticia-segundaria"]//div[@class="left"]//a')
    urls = ['https://www.elcolombiano.com/' + i.get('href') for i in urls]
    titulos = [i.text for i in titulos]
    categorias = dom.xpath('//div[@class="noticia-segundaria"]//div[@class="right"]//div[@class="categoria-noticia"]//a')
    categorias = [i.text for i in categorias]
    for i in range(len(imagenes)):
        collection.insert_one({"imagen": imagenes[i], "titulo": titulos[i], "url": urls[i],"categoria": categorias[i], "fecha": fecha, "fuente": "El Colombiano"})
        allNoticias.append([imagenes[i], titulos[i], urls[i], categorias[i]])

# Ya funciona
if(elHeraldo.status_code == 200):
    soup = BeautifulSoup(elHeraldo.content, 'html.parser')
    dom = etree.HTML(str(soup))
    titulos = dom.xpath('//article[@class="item horizontal foto-titulo-sumario small"]//div[@class="text"]//h1//a')
    imagenes = dom.xpath('//article[@class="item horizontal foto-titulo-sumario small"]//div[@class="image"]//img')
    imagenes = [i.get('src') for i in imagenes]
    urls = dom.xpath('//article[@class="item horizontal foto-titulo-sumario small"]//h1//a')
    urls = ['https://www.elheraldo.co' + i.get('href') for i in urls]
    titulos = [i.text for i in titulos]
    categorias = dom.xpath('//article[@class="item horizontal foto-titulo-sumario small"]//div[@class="text"]//div[@class="datos"]//span[1]')
    categorias = [i.text for i in categorias]
    for i in range(len(imagenes)):
        collection.insert_one({"imagen": imagenes[i], "titulo": titulos[i], "url": urls[i],"categoria": categorias[i], "fecha": fecha, "fuente": "El Heraldo"})
        allNoticias.append([imagenes[i], titulos[i], urls[i], categorias[i]])

print(allNoticias)