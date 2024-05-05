from fastapi import FastAPI, Query
import requests#

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    """
    Um endpoint que mostra uma mensagem famosa no inicio da programação
    """
    return {'hello':'world'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint que mostra os cardápios dos restaurante
    """
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return{'Restaurante':restaurante, 'Cardapio':dados_restaurante}
    else: 
        return{'Erro':f'{response.status.code} - {response.text}'}
