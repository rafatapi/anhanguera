import socket

# Cria um socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço IP e a porta do servidor
host = 'localhost'
port = 8888

# Conecta ao servidor
client_socket.connect((host, port))

# Envia uma mensagem ao servidor
message = 'Olá, servidor'
client_socket.sendall(message.encode())

# Recebe a mensagem de confirmação do servidor
data = client_socket.recv(1024).decode()

print(f'Mensagem do servidor: {data}')

# Encerra a conexão
client_socket.close()
