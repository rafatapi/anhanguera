import time
import subprocess

# Caminho do Programa 2
caminho_programa2 = r"D:\git-gcp\paralelo\2024S1-U2\u2s2-passagem\ex03-pipes-02.py"

# Escreve uma mensagem no pipe com codificação UTF-8
mensagem = "Olá, Programa XPTO!".encode('utf-8')

# Cria um subprocesso para executar o Programa 2
pipe = subprocess.Popen(["python", caminho_programa2], stdin=subprocess.PIPE)

# Escreve a mensagem no pipe
pipe.stdin.write(mensagem)
pipe.stdin.close()

time.sleep(2)  # Aguarda um pouco para o Programa 2 responder