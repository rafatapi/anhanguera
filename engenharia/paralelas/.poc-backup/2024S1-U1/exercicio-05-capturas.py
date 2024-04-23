import requests
import json
import pandas as pd
from tqdm import tqdm
from time import sleep, time
from multiprocessing.pool import ThreadPool
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import sys


# funcao de log com datahora
def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:23]
    print(f"[{timestamp}] :: {message}")    


# funcao para fazer um request dos dados de um deputado
def detalhe_deputado(id):
    url        = 'https://dadosabertos.camara.leg.br/api/v2/deputados/' + id
    parametros = {}
    resposta   = requests.request("GET", url, params=parametros)
    objetos    = json.loads(resposta.text)
    dados      = objetos['dados']
    return dados

# definindo uma variavel para a quantidade de registros para buscar
quantidade_max = 100

# inicio da execucao
log('------------------------------------------------------------------------------------')
log('INICIO')
log('------------------------------------------------------------------------------------')

# Requisição dos dados dos Deputados
log("Consulta na API de Dados Abertos da Camara dos Deputados")
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?pagina=1&itens='+str(quantidade_max)
parametros = {}
resposta   = requests.request("GET", url, params=parametros)
if (resposta.text == "upstream request timeout"):
    log(resposta.text+" - tente novamente")
    sys.exit(500)
log("Lendo resposta da API")
objetos    = json.loads(resposta.text)
dados      = objetos['dados']
log("Todos os dados foram lidos")

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Selecionando todos os ids dos deputados
log("Selecionando todos os ids dos deputados")
id = []
for i in range(len(dados)):
    id.append(str(dados[i]['id']))

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


"""
print("Requisição dos detalhes de um deputado")
inicio_processo = time()
deputado = detalhe_deputado('204521')
fim_processo = time()
processamento_individual = fim_processo - inicio_processo
print('Processamento individual por id:', round( (processamento_individual), 1 ), 'segundos')
print('------------------------------------------------------------------------------------')
"""

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# definicao da quantidade
ids = id[:quantidade_max]

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# registros - sequenciais
log('')
log('Processamento sequencial - START')
inicio_processo = time()
lista_api_sequencial = []
for i in tqdm(ids):
    resultado_individual = detalhe_deputado(i)
    lista_api_sequencial.append(resultado_individual)
fim_processo = time()
processamento_sequencial = fim_processo - inicio_processo
log('Processamento sequencial por id:'+str(round( (processamento_sequencial), 1 ))+'segundos')
log('Processamento sequencial - FINISH')


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# registros - paralelo
# Subprocessos para requisição em paralelo na API
log('')
log('Processamento paralelo - START')
inicio_processo = time()
lista_subprocessos = []
pool = ThreadPool(processes=10)
 
for i in tqdm(ids):
    subprocesso_executando = pool.apply_async(detalhe_deputado, (i, ))
    lista_subprocessos.append(subprocesso_executando)

# Lista para armazenar os resultados das requisições
lista_resultados_api = []

log('Processamento paralelo - Aguardando resultados')

# Loop para iterar sobre os futuros resultados
for futuro_resultado in tqdm(lista_subprocessos):
    # Obtém o resultado da requisição 
    resultado_api = futuro_resultado.get(timeout=60)
    # Adiciona o resultado à lista
    lista_resultados_api.append(resultado_api)


# lista_api_paralela = [result.get(timeout=120) for result in tqdm(subprocessos)]
 
fim_processo = time()
processamento_paralelo = fim_processo - inicio_processo
log('Processamento paralelo dos id: '+str( round( (processamento_paralelo), 1 ))+ 'segundos')
log('Processamento paralelo - FINISH ('+str(len(lista_resultados_api))+')')

