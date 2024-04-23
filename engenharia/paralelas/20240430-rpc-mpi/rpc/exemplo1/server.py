import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = '127.0.0.1'
port = 8000

server.bind((hostname, port))
server.listen(5)
conn, addr = server.accept()

while True:
    data = conn.recv(1024).decode('utf-8')
    if not data:
        break

    # Processa a mensagem recebida e realiza a operação matemática
    operation, num1, num2 = data.split(',')
    if operation == 'add':
        result = int(num1) + int(num2)
    elif operation == 'subtract':
        result = int(num1) - int(num2)

    conn.send(str(result).encode('utf-8'))

conn.close()
server.close()