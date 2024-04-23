# 2. Exemplo com fila (queue):
import multiprocessing

def increment(queue, n):
    total = 0
    for _ in range(n):
        total += 1
    queue.put(total)  # Adiciona o total na fila

if __name__ == '__main__':
    queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=increment, args=(queue, 1000))
    process2 = multiprocessing.Process(target=increment, args=(queue, 1000))
    process3 = multiprocessing.Process(target=increment, args=(queue, 1000))
    process4 = multiprocessing.Process(target=increment, args=(queue, 1000))
    process5 = multiprocessing.Process(target=increment, args=(queue, 1000))

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

    total = 0
    while not queue.empty():
        total += queue.get()

    print(f'Total acumulado na fila: {total}')

