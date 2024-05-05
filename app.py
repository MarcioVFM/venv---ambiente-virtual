import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
#url do arquivo JSON com varios dados de restaurantes

response = requests.get(url)#pega os dados da url
print(response) #printa response [200], a solicitacao foi atendida com sucesso

if response.status_code == 200:#caso ela retorne 200, indicando que funcionou
    dados_jason = response.json()
    dados_restaurante = {}
    for item in dados_jason:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            "item":item['Item'],
            "price":item['price'],
            "description":item['description']
            })
        
else:
    print(f'O erro foi o {response.status_code}')

#print(dados_restaurante["Pizza Hut"])
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)