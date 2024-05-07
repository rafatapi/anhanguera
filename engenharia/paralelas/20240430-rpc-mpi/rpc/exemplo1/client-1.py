import socket

# Cria um socket TCP/IP para o cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço e a porta do servidor que o cliente irá se conectar
hostname = '127.0.0.1'
port = 8000

# Conecta-se ao servidor utilizando o endereço e a porta especificados
client.connect((hostname, port))

# Cria uma mensagem com a operação e os argumentos a serem enviados ao servidor
message = 'add,10,3'  # Mensagem contendo a operação e os argumentos

# Envia a mensagem codificada em UTF-8 para o servidor
client.send(message.encode('utf-8'))

# Recebe o resultado da operação enviada pelo servidor e decodifica para UTF-8
result = client.recv(1024).decode('utf-8')

# Imprime o resultado da operação
print("Resultado da operação:", result)

# Fecha a conexão com o servidor
client.close()