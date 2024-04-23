import socket
import requests
import json

def buscar_nome_lider(id_partido):
    response = requests.get(f'https://dadosabertos.camara.leg.br/api/v2/partidos/{id_partido}')
    partido_data = response.json()
    lider_partido = partido_data['dados']['status']['lider']['nome']
    return lider_partido

# Configuração do socket
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 12345))
    print("Servidor está no ar e aguardando conexões...")
    s.listen()

    while True:
        client, address = s.accept()
        print("Conexão estabelecida com:", address)

        # Recebe o id do partido do cliente
        id_partido = client.recv(1024).decode()
        print("ID do partido recebido:", id_partido)

        # Busca o nome do líder do partido e envia de volta para o cliente
        nome_lider = buscar_nome_lider(id_partido)
        client.send(nome_lider.encode())

        client.close()

if __name__ == "__main__":
    main()