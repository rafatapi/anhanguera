import socket

# Cria um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define a porta e o endereço IP
host = 'localhost'
port = 8888

# Liga o socket ao endereço e à porta
server_socket.bind((host, port))

# Coloca o socket em modo de escuta
server_socket.listen()

print(f'Servidor escutando em {host} na porta {port}')

# Aceita a conexão do cliente
client_socket, client_address = server_socket.accept()

print(f'Conexão estabelecida com {client_address}')

# Recebe a mensagem do cliente
data = client_socket.recv(1024).decode()

print(f'Mensagem do cliente: {data}')

# Envia uma mensagem de confirmação ao cliente
client_socket.sendall('Mensagem recebida pelo servidor'.encode())

# Encerra a conexão
client_socket.close()
server_socket.close()
