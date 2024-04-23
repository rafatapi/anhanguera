import requests
import socket
import threading
import time

start_time = time.time()

# Função para a comunicação com o servidor
def get_lider_por_id(id_partido, sigla):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 12345))

    # Envia o id do partido para o servidor
    s.send(str(id_partido).encode())

    # Recebe e imprime o nome do líder do partido
    nome_lider = s.recv(1024).decode()
    print(f"Líder do partido com ID {id_partido} ({sigla}): {nome_lider}")

    s.close()

# Busca todas as siglas dos partidos na API
response = requests.get('https://dadosabertos.camara.leg.br/api/v2/partidos')
partidos = response.json()['dados']

# Cria uma thread para cada chamada ao servidor
threads = []
for partido in partidos:
    id_partido = partido['id']
    sigla = partido['sigla']
    thread = threading.Thread(target=get_lider_por_id, args=(id_partido,sigla))
    threads.append(thread)
    thread.start()

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

# calcula o tempo
print(f"Tempo decorrido: {time.time()- start_time} segundos")
