# 1. Exemplo com variável comum:

import multiprocessing

# Função para incrementar uma variável comum compartilhada
def increment(counter):
    for _ in range(1000):
        counter.value += 1

if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)  # Variável compartilhada

    # Cria dois processos para incrementar a variável
    process1 = multiprocessing.Process(target=increment, args=(counter,))
    process2 = multiprocessing.Process(target=increment, args=(counter,))
    process3 = multiprocessing.Process(target=increment, args=(counter,))
    process4 = multiprocessing.Process(target=increment, args=(counter,))
    process5 = multiprocessing.Process(target=increment, args=(counter,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()


    print(f'Valor final da variável comum: {counter.value}')