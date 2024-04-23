import multiprocessing

# Função para incrementar uma variável comum compartilhada
def increment(counter):
    for _ in range(1000):
        counter.value += 1

if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)  # Variável compartilhada
    num_processos = 10  # Número de processos
    processos = []  # Lista para armazenar os processos

    # Cria e adiciona os processos à lista
    for i in range(1, num_processos + 1):
        processo = multiprocessing.Process(target=increment, args=(counter,))
        processos.append(processo)

    # Inicia os processos
    for processo in processos:
        processo.start()

    # Aguarda a conclusão de todos os processos
    for processo in processos:
        processo.join()


    print(f'Valor final da variável compartilhada: {counter.value}')