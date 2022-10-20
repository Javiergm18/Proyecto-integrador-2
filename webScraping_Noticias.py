# from sre_constants import SUCCESS
import requests
from bs4 import BeautifulSoup
from lxml import etree
from pymongo import MongoClient
import datetime

fecha = str(datetime.date.today())

cluster = MongoClient("mongodb+srv://usuario1:upbbga2021.@cluster0.a87koto.mongodb.net/?retryWrites=true&w=majority")

db = cluster['integrador']
collection = db['noticias']

# mongoHost = 'mongodb://localhost'
# client = MongoClient(mongoHost)

# db = client['integrador2']
# collection = db['noticias']

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
        allNoticias.append([imagenes[i], titulos[i], urls[i], categorias[i], (titulos[i] + ", " + categorias[i]), "El tiempo"])
    
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
        allNoticias.append([imagenes[i], titulos[i], urls[i], categorias[i], (titulos[i] + ", " + categorias[i]), "Pulzo"])

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
        allNoticias.append([imagenes[i], titulos[i], urls[i], categorias[i], (titulos[i] + ", " + categorias[i]), "El Colombiano"])

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
        allNoticias.append([imagenes[i], titulos[i], urls[i], categorias[i], (titulos[i] + ", " + categorias[i]), "El Heraldo"])

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sw = stopwords.words('spanish')

categorias = ['Deportes mundial fútbol Messi tenis Qatar goleada deportivo ganó libertadores champions liga', 
              'Economía Silicon Valley tarifas subsidios reforma tributaria subsidiar recursos hacienda presupuesto corrupción precio dólar dolares pesos encuesta empresa Gustavo Petro Colombia colombiana salario', 
              'Entretenimiento tiktok tiktoker instagram instagramer influencer música denuncias despecho ritmo famoso shakira pareja reina belleza amante corazón entusado canciones', 
              'Política personero personería diálogos paz ELN Duque Maduro políticos embajador embajadora embajadores colombianos denuncias gobernación história Bogotá gobernar policía uniformados mundo primera primer ministro ministra mundo renunció renuncia cargo corrupción gobierno violencia Bogotá Colombia Gustavo desaprobación roban robar Petro líder nación país narcotráfico conclicto empresarios libremente presidente encuesta', 
              'Cultura educación universidad academia profesor cósmico creación estudiantes', 
              'Salud engordar engordando covid covid-19 pandemia vacuna vacunación ciencia encuesta desnutrición nutrición']

for i in range(len(allNoticias)):
    X_list = word_tokenize(allNoticias[i][4].lower())
    X_set = {w for w in X_list if not w in sw}
    cosines = []
    for j in range(len(categorias)):
        Y_list = word_tokenize(categorias[j].lower())
        Y_set = {w for w in Y_list if not w in sw}
        l1 =[]
        l2 =[]
        rvector = X_set.union(Y_set) 
        for w in rvector:
            if w in X_set: l1.append(1) # create a vector
            else: l1.append(0)
            if w in Y_set: l2.append(1)
            else: l2.append(0)
        c = 0
        # cosine formula 
        for k in range(len(rvector)):
            c+= l1[k]*l2[k]
        division = float((sum(l1)*sum(l2))**0.5)
        if(division != 0):
            cosine = c / division
            cosines.append(cosine)
        else:
            cosines.append(0)
    mayor = cosines[0]
    indexMayor = 0
    contCeros = 0
    for j in range(0, len(cosines)):
        if(mayor < cosines[j]):
            mayor = cosines[j]
            indexMayor = j
        if(cosines[j] == 0):
            contCeros += 1
    if(contCeros == 6):
        allNoticias[i][3] = 'Otras'
    else:
        if(indexMayor == 0):
            allNoticias[i][3] = 'Deportes'
        elif(indexMayor == 1):
            allNoticias[i][3] = 'Economía'
        elif(indexMayor == 2):
            allNoticias[i][3] = 'Entretenimiento'
        elif(indexMayor == 3):
            allNoticias[i][3] = 'Política'
        elif(indexMayor == 4):
            allNoticias[i][3] = 'Cultura'
        elif(indexMayor == 5):
            allNoticias[i][3] = 'Salud'

import random
random.shuffle(allNoticias)

for i in range(len(allNoticias)):
    collection.insert_one({"imagen": allNoticias[i][0], "titulo": allNoticias[i][1], "url": allNoticias[i][2],"categoria": allNoticias[i][3], "fecha": fecha, "fuente": allNoticias[i][5]})

print(allNoticias)