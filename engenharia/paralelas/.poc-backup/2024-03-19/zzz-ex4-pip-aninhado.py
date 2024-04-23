import threading
import subprocess

def producer():
    for i in range(10):
        message = f"Mensagem {i}"
        print(f"Produtor enviando: {message}")

        # Cria um pipe aninhado para comunicação bidirecional
        with subprocess.Popen(['cat'], stdout=subprocess.PIPE, stdin=subprocess.PIPE) as pipe:
            # Envia a mensagem para o pipe
            pipe.stdin.write(message.encode('utf-8') + b'\n')
            pipe.stdin.flush()

            # Recebe a resposta do consumidor
            response = pipe.stdout.readline().decode('utf-8').strip()
            print(f"Produtor recebendo: {response}")

def consumer():
    with subprocess.Popen(['echo'], stdin=subprocess.PIPE, stdout=subprocess.PIPE) as pipe:
        while True:
            # Recebe a mensagem do produtor
            message = pipe.stdin.readline().decode('utf-8').strip()
            print(f"Consumidor recebendo: {message}")

            # Envia uma resposta para o produtor
            response = f"Mensagem recebida: {message}"
            pipe.stdout.write(response.encode('utf-8') + b'\n')
            pipe.stdout.flush()

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


"""
Explicação:

    Este código usa um pipe aninhado para comunicação bidirecional entre o produtor e o consumidor.
    Um pipe aninhado consiste em dois pipes, um para cada direção da comunicação.
    O produtor envia mensagens para o pipe de entrada do consumidor e recebe respostas do pipe de saída do consumidor.
    O consumidor recebe mensagens do pipe de entrada do produtor e envia respostas para o pipe de saída do produtor.

"""