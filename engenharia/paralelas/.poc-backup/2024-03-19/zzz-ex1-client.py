import socket

# Cria um socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o IP e a porta do servidor
server_ip = '127.0.0.1'
server_port = 1234

# Conecta ao servidor
client_socket.connect((server_ip, server_port))

# Envia uma mensagem para o servidor
message = "Olá, servidor!"
client_socket.send(message.encode())

# Recebe a resposta do servidor
response = client_socket.recv(1024).decode()
print(f"Resposta do servidor: {response}")

# Fecha a conexão com o servidor
client_socket.close()