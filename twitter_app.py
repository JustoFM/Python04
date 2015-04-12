#!/usr/bin/python
# -*- coding: utf-8 -*

# <codecell>

# Sistemas Distribuidos
# Seminario 4

# Autores:
#   Justo Manuel Fuentes Meléndez
#   Christian Suárez Picón

#Importamos los paquetes que necesitemos
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

import twitter

app = Flask(__name__)
GoogleMaps(app)
coordenadas=[]

CONSUMER_KEY = 'jEu4devPZPSOFjaiRREMt8MQ1'
CONSUMER_SECRET = 'jKy0hnGiWz8x5JPreBnELB6EI0Mz3r7YK8FHdLhE3O1TgAJS7B'
OAUTH_TOKEN = '326450822-WtwzTbfuVDqlHS63r2GmPSWdJRlmMrnIIt8J4V6p'
OAUTH_TOKEN_SECRET = 'SYyMRKEnI9Fy928tvmkG1NzhsXLBmpYh1sAjS3NV2iKME'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

#Almacenos los tweets que tengan estas caracteristicas
search_results = twitter_api.search.tweets(q='Cadiz',geocode='40.45,-3.75,1000km')

for result in search_results["statuses"]:
    if result["geo"]:
        x=result["geo"]["coordinates"][0]
        y=result["geo"]["coordinates"][1]
        pair=[x,y]
        coordenadas.append(pair)

#Creamos el Mapa con los valores que queramos
@app.route("/")
def mapview():
    mymap = Map(
        identifier="view-side",
        lat=40.45,
        lng=3.75,
        markers=coordenadas,
        style="height:600px;width:600px;margin:0", 
        zoom=4
    )
    return render_template('mymap.html', mymap=mymap)

#Ejecutamos la App
if __name__ == "__main__":
    app.run(debug=True)
    
# <codecell>