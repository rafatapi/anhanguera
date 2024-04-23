import sys

# Lê a mensagem do pipe em UTF-8
mensagem = sys.stdin.buffer.read().decode('utf-8')
mensagem = f"Mensagem recebida pelo Programa 2: {mensagem.upper()}"

# Exibe a mensagem recebida pelo Programa 2 em letras maiúsculas
sys.stdout.buffer.write(mensagem.encode('utf-8'))
sys.stdout.buffer.flush()

# Fecha o buffer de entrada
sys.stdin.buffer.close()

# Fecha o buffer de saída
sys.stdout.buffer.close()

