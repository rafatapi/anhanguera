# https://cienciadacomputacao.wiki.br/25_Tecnologia_Sistemas_Distribuidos.html

from threading import Thread

# Número de processos
n = 10

# Variáveis ​​compartilhadas (use um lock para cenários reais)
entrando = [False] * n  # Indica se um processo está tentando entrar na seção crítica
numeros = [0] * n      # Números de tíquete atribuídos aos processos

def padaria(id_processo):
    """
    Implementação do algoritmo de Bakery para exclusão mútua.

    Args:
        id_processo (int): A ID do processo atual.
    """

    global entrando, numeros  # Acesso a variáveis ​​compartilhadas

    # 1. Fase de Entrada
    entrando[id_processo] = True  # Marca o processo como tentando entrar
    numeros[id_processo] = max(numeros) + 1  # Obter um número de tíquete (mais alto + 1)

    # 2. Fase de Espera
    entrando[id_processo] = False  # Redefinir a bandeira de entrada (importante!)

    for j in range(n):
        # Espere por qualquer processo já na seção crítica
        while entrando[j]:
            pass

        # Espere por processos com números de tíquete mais baixos ou o mesmo número com um ID menor
        while numeros[j] != 0 and (numeros[j], j) < (numeros[i], id_processo):
            pass

    # Seção Crítica (simulada com uma instrução print)
    print(f"Processo {id_processo} entrou na seção crítica")
    # Seu código real da seção crítica iria aqui (acesso a recursos compartilhados)

    # 3. Fase de Saída
    numeros[id_processo] = 0  # Liberar o número do bilhete

# Criação e inicialização de threads
threads = []
for i in range(n):
    threads.append(Thread(target=padaria, args=(i,)))

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Todos os processos terminaram.")
