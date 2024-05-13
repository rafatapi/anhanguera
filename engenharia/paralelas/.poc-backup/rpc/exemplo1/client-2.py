import socket
import threading

def client_request(hostname, port, message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((hostname, port))
    client.send(message.encode('utf-8'))
    result = client.recv(1024).decode('utf-8')
    print("Resultado da operação:", result)
    client.close()

hostname = '127.0.0.1'
port = 8000

# Mensagem contendo a operação e os argumentos a serem enviados ao servidor
message = 'add,10,3'

# Lista para armazenar as threads
threads = []

# Número de chamadas que serão feitas
num_calls = 100

# Cria e inicia threads para realizar as chamadas ao servidor
for _ in range(num_calls):
    thread = threading.Thread(target=client_request, args=(hostname, port, message))
    thread.start()
    threads.append(thread)

# Espera todas as threads terminarem
for thread in threads:
    thread.join()