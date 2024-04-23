import multiprocessing

# Função que será executada pelos processos
def worker(shared_array, value):
    shared_array[value] = value

if __name__ == '__main__':
    # Criando um array compartilhado entre os processos
    shared_array = multiprocessing.Array('i', 10)

    # Criando os processos
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=worker, args=(shared_array, i))
        p.start()
        processes.append(p)

    # Esperando os processos terminarem
    for p in processes:
        p.join()

    # Exibindo o array compartilhado após a execução dos processos
    print(list(shared_array))


"""
Neste exemplo, criamos um array compartilhado de integers com tamanho 10. Em seguida, 
criamos 10 processos que executam a função `worker`, passando o array compartilhado e
um valor como argumentos. Cada processo vai escrever seu valor no array compartilhado.

Após a execução dos processos, exibimos o conteúdo do array compartilhado para ver os
valores que foram escritos por cada processo.

É importante ressaltar que ao trabalhar com memória compartilhada, devemos garantir 
a consistência dos dados e evitar problemas de concorrência. Para isso, é fundamental 
utilizar mecanismos de sincronização, como semáforos, locks ou filas.

Este é apenas um exemplo simples de como programar com memória compartilhada em Python 
utilizando o módulo `multiprocessing`. Com um pouco mais de prática e estudo, é possível 
desenvolver aplicações mais complexas e eficientes utilizando esse recurso.
"""