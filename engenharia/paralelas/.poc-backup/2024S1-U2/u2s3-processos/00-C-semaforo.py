import multiprocessing
from multiprocessing import Semaphore

# Função para incrementar uma variável comum compartilhada
def increment(counter, semaforo):
    for _ in range(1000):
        semaforo.acquire()  # Adquire o semáforo antes de acessar a variável
        counter.value += 1
        semaforo.release()  # Libera o semáforo após a atualização

if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)  # Variável compartilhada
    semaforo = Semaphore(1)  # Semáforo com capacidade 1 (exclusão mútua)

    num_processos = 10  # Número de processos
    processos = []  # Lista para armazenar os processos

    # Cria e adiciona os processos à lista
    for _ in range(num_processos):
        processo = multiprocessing.Process(target=increment, args=(counter, semaforo))
        processos.append(processo)

    # Inicia os processos
    for processo in processos:
        processo.start()

    # Aguarda a conclusão de todos os processos
    for processo in processos:
        processo.join()

    print(f'Valor final da variável compartilhada: {counter.value}')