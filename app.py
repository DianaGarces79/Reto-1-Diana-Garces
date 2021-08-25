# importar flask
from flask import Flask, Response
# importando la libreira request
import requests
# importando la libreria json
import json
# inicializando una aplicacion de flask
app = Flask(__name__)
# ruta por defecto para entrar a la aplicacion
@app.route("/")
def hello_world():
    return "<p>Hola mundo!</p>" # HTML

# API de Yahoo Finance
@app.route("/get-price/<ticker>")
# Define la funcion que va a ejecutar esta ruta
def get_price(ticker): #parametro ticker
    #dirección de la API
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    # encabezado de la petición
    headers={'User-Agent': 'Mozilla/5.0'}
    # se asgina la respuesta a la variable response
    response = requests.get(url,headers=headers)
    # se convierte a .json
    company_info = response.json()
    #Imprimo los datos del json
    print(company_info)
    # se extraen los datos de interés
    price = company_info['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
    company_name = company_info['quoteSummary']['result'][0]['price']['longName']
    exchange = company_info['quoteSummary']['result'][0]['price']['exchangeName']
    currency = company_info['quoteSummary']['result'][0]['price']['currency']
    # configuro los datos en .json
    result = {
        "price": price,
        "name": company_name,
        "exchange": exchange,
        "currency": currency
    }
    print(result) #imprimo los datos en consola

    return Response(json.dumps(result))# retorno los datos al cliente

if __name__ == '__main__':
    app.run()
