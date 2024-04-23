import socket
import requests
import json
from concurrent.futures import ThreadPoolExecutor

def buscar_nome_lider(id_partido):
    response = requests.get(f'https://dadosabertos.camara.leg.br/api/v2/partidos/{id_partido}')
    partido_data = response.json()
    
    lider_partido = partido_data['dados']['status']['lider']['nome']
    return lider_partido

def handle_client(client, address):
    print("Conexão estabelecida com:", address)
    
    try:
        id_partido = client.recv(1024).decode()
        print("ID do partido recebido:", id_partido)
        nome_lider = buscar_nome_lider(id_partido)
        client.send(nome_lider.encode())
        
    except Exception as e:
        print("Erro ao processar requisição:", e)
    
    client.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 12345))
    print("Servidor está no ar e aguardando conexões...")
    s.listen()
    
    with ThreadPoolExecutor(max_workers=10) as executor:  # Pode ajustar o número de threads conforme necessário
        while True:
            client, address = s.accept()
            executor.submit(handle_client, client, address)

if __name__ == "__main__":
    main()