import socket
import threading

def producer():
    HOST = "localhost"  # Endereço do servidor
    PORT = 8000  # Porta do servidor

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conecta ao servidor
        sock.connect((HOST, PORT))

        for i in range(10):
            message = f"Mensagem {i}"
            print(f"Produtor enviando: {message}")

            # Envia a mensagem para o servidor
            sock.sendall(message.encode('utf-8'))

            # Recebe a resposta do servidor
            response = sock.recv(1024).decode('utf-8')
            print(f"Produtor recebendo: {response}")

def consumer():
    HOST = "localhost"  # Endereço do servidor
    PORT = 8000  # Porta do servidor

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conecta ao servidor
        sock.connect((HOST, PORT))

        while True:
            # Recebe a mensagem do produtor
            message = sock.recv(1024).decode('utf-8')
            print(f"Consumidor recebendo: {message}")

            # Envia uma resposta para o produtor (implemente a lógica de resposta aqui)
            # Exemplo:
            response = f"Mensagem recebida: {message}"
            sock.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


"""
Explicação - Sockets:

    Sockets são um mecanismo de comunicação de rede mais robusto e flexível do que pipes.
    Eles permitem comunicação bidirecional entre processos em execução em diferentes máquinas (não apenas no mesmo programa).
    O código implementa um socket TCP (Transmission Control Protocol) para comunicação confiável e orientada a fluxo.
    O produtor e o consumidor se conectam a um servidor em execução na mesma máquina (localhost) na porta 8000.
    O produtor envia mensagens para o servidor e recebe respostas. O consumidor faz o mesmo.
    O servidor (que não está implementado neste exemplo) seria responsável por rotear as mensagens entre produtor e consumidor.

"""