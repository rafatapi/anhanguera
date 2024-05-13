import socket

# Cria um socket TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço e a porta que o servidor irá escutar
hostname = '127.0.0.1'
port = 8000
print(f"Servidor rodando em {hostname}:{port}")

# Atribui o endereço e a porta ao socket
server.bind((hostname, port))

# Habilita o servidor para escutar conexões. O argumento é o número de clientes em espera na fila
server.listen(5)

# Loop principal para receber e processar dados do cliente
while True:

    # Aceita a conexão e pega o endereço do cliente
    conn, addr = server.accept()

    # Recebe os dados do cliente e decodifica-os para utf-8
    data = conn.recv(1024).decode('utf-8')
    if not data:
        continue

    # Processa a mensagem recebida e realiza a operação matemática
    operation, num1, num2 = data.split(',')
    if operation == 'add':
        result = int(num1) + int(num2)
    elif operation == 'subtract':
        result = int(num1) - int(num2)

    # Envia o resultado da operação de volta para o cliente
    conn.send(str(result).encode('utf-8'))

# Fecha a conexão e o socket do servidor
#conn.close()
#server.close()