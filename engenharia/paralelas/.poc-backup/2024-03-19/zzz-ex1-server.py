import socket

# Cria um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o IP e a porta do servidor
server_ip = '127.0.0.1'
server_port = 1234

# Liga o socket ao IP e porta especificados
server_socket.bind((server_ip, server_port))

# Habilita o servidor para aceitar conexões
server_socket.listen()

print(f"Servidor ouvindo em {server_ip}:{server_port}")

while True:
    # Aceita a conexão do cliente
    client_socket, client_address = server_socket.accept()

    # Recebe a mensagem do cliente
    message = client_socket.recv(1024).decode()
    print(f"Mensagem recebida do cliente: {message}")

    # Envia uma resposta para o cliente
    client_socket.send("Mensagem recebida pelo servidor".encode())

    # Fecha a conexão com o cliente
    client_socket.close()