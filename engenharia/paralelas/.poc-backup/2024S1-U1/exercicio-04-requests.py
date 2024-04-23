import os
import requests
from datetime import datetime
from time import time
from multiprocessing.pool import ThreadPool

# urls
urls = (
    'http://www.estadao.com',
    'http://www.terra.com.br',
    'http://www.uol.com.br',
    'http://www.globo.com',
    'http://www.folha.com.br',
    'http://www.bbc.com',
    'http://www.cnn.com',
    'http://www.lance.com.br',
    'http://www.gov.br',
    'http://www.gooogle.com',
    'http://www.yahoo.com',
    'http://www.microsoft.com',
)

print(f"[{datetime.now()}] :: -------------------------------------------------------------------------------")
print(f"[{datetime.now()}] :: 1 request")
print(f"[{datetime.now()}] :: -------------------------------------------------------------------------------")
start = time()

# exemplo - 1 request
print(f"[{datetime.now()}] :: REQUEST - Inicio : {urls[1]}")
response = requests.get(urls[1])
print(f"[{datetime.now()}] :: REQUEST - Fim    : {urls[1]}")

print(f"[{datetime.now()}] :: Tempo total: {(time() - start)}")


print(f"[{datetime.now()}] :: -------------------------------------------------------------------------------")
print(f"[{datetime.now()}] :: requests - sequenciais")
print(f"[{datetime.now()}] :: -------------------------------------------------------------------------------")
start = time()


for url in urls:
    print(f"[{datetime.now()}] :: REQUEST - Inicio : {url}")
    response = requests.get(url)
    print(f"[{datetime.now()}] :: REQUEST - Fim    : {url}")


print(f"[{datetime.now()}] :: Tempo total: {(time() - start)}")

print(f"[{datetime.now()}] :: -------------------------------------------------------------------------------")
print(f"[{datetime.now()}] :: requests - paralelos")
print(f"[{datetime.now()}] :: -------------------------------------------------------------------------------")
start = time()
# exemplo - 4 requests paralelos

def get_request_by_url(url):
    print(f"[{datetime.now()}] :: REQUEST - Inicio : {url}")
    response = requests.get(url)
    print(f"[{datetime.now()}] :: REQUEST - Fim    : {url} - {response.status_code}")
    
threads_executando = []
pool = ThreadPool(processes=10)
pool.map(get_request_by_url, urls)

print(f"[{datetime.now()}] :: Tempo total: {(time() - start)}")

print(f"[{datetime.now()}] :: -------------------------------------------------------------------------------")
print(f"[{datetime.now()}] :: -------------------------------------------------------------------------------")

