import socket
import time
import datetime

# Criar um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define a porta e o endereço IP
host = 'localhost'
port = 8888

# Vincular o socket a porta
server_socket.bind((host, port))

# Esperar por conexao
server_socket.listen(1)
print(f'Servidor escutando em {host} na porta {port}')

while True:
    # Aceitar conexao
    client_socket, client_address = server_socket.accept()
    intervalo = client_socket.recv(1024).decode()
    intervalo = int(intervalo)
    print('Conectado por', client_address)

    while True:
        # Obter a data/hora atual
        now = datetime.datetime.now()

        # Enviar a data/hora atual para o cliente
        client_socket.send(str(now).encode())

        time.sleep(intervalo)  # aguardar 5 segundos

