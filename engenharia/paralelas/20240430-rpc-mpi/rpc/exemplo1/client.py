import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = '127.0.0.1'
port = 8000

client.connect((hostname, port))
message = 'add,5,3'  # Mensagem contendo a operação e os argumentos
client.send(message.encode('utf-8'))

result = client.recv(1024).decode('utf-8')
print("Resultado da operação:", result)

client.close()