import socket
import threading

HOST = "localhost"  # Endereço do servidor
PORT = 8000  # Porta do servidor

def handle_client(client_socket):
    while True:
        # Recebe a mensagem do cliente
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break

        print(f"Cliente {client_socket.getpeername()} enviou: {message}")

        # Processa a mensagem (implemente a lógica de processamento aqui)
        # Exemplo:
        response = f"Mensagem recebida: {message}"

        # Envia a resposta para o cliente
        client_socket.sendall(response.encode('utf-8'))

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)

        print(f"Servidor escutando em {HOST}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Cliente conectado: {client_address}")

            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

if __name__ == "__main__":
    main()


"""
Explicação:

    Este código implementa um servidor simples que escuta na porta 8000 e aceita conexões de clientes.
    A função handle_client é responsável por:
        Receber a mensagem do cliente.
        Processar a mensagem (implemente a lógica de processamento aqui).
        Enviar a resposta para o cliente.
    A função main cria um socket de servidor, escuta em uma porta e aceita conexões de clientes.
    Para cada cliente conectado, uma thread é criada para lidar com a comunicação com o cliente.

Observações:

    Este é um servidor básico para demonstrar o funcionamento de sockets.
    Você pode aprimorar o código para:
        Implementar diferentes tipos de processamento de mensagens.
        Tratar erros de forma mais robusta.
        Manter um registro de clientes conectados.

"""
