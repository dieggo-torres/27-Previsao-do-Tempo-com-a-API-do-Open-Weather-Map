# Importa a biblioteca os
import os

# Importa a biblioteca requests
import requests

# Importa um método da biblioteca dotenv
from dotenv import load_dotenv

# Carreaga as variáveis de ambiente
load_dotenv()

# Obtém o token de acesso à API
api_key = os.getenv('API_KEY')

# Solicita que o usuário digite o nome de uma cidade
cidade = input('Digite o nome de uma cidade:\n')

# Unidades de medida
unidades = 'metric'

# Idioma de exibição (português brasileiro)
idioma = 'pt_BR'

# Link para fazer a requisição
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&units={unidades}&lang={idioma}&appid={api_key}'

# Faz uma requisição do tipo GET
requisicao = requests.get(link)

# Converte a resposta da requisição para o formato JSON
requisicao_dic = requisicao.json()

# Exibição de resultados
print(f"Cidade: {requisicao_dic['name']}")
print(f"Descrição: {requisicao_dic['weather']['description']}")
print(f"Temperatura: {requisicao_dic['main']['temp']}")
print(f"Sensação térmica: {requisicao_dic['main']['feels_like']}")
print(f"Temperatura mínima: {requisicao_dic['main']['temp_min']}")
print(f"Temperatura máxima: {requisicao_dic['main']['temp_max']}")