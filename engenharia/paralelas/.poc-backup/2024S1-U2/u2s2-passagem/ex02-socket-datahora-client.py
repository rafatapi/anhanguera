import socket

# Criar um socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar ao servidor
client_socket.connect(('localhost', 8888))

# Pedir ao usuário quantos segundos deseja receber a informação
intervalo = int(input('Informe de quantos em quantos segundos deseja receber a informação: '))

# Enviar o intervalo para o servidor
client_socket.send(str(intervalo).encode())

while True:
    # Receber a data/hora atual do servidor
    data = client_socket.recv(1024)

    print('Data/hora atual:', data.decode())

# Fechar conexao
client_socket.close()