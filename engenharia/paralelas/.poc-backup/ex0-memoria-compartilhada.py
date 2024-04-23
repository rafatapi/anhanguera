import multiprocessing

# Função que adiciona um número à lista
def add_number(numbers, number):
    numbers.append(number)

if __name__ == '__main__':
    # Criando uma lista compartilhada entre os processos
    numbers = multiprocessing.Manager().list()
    numbers.append(1)  # Adicionando o número 1 à lista inicialmente

    # Criando dois processos que chamam a função add_number
    process1 = multiprocessing.Process(target=add_number, args=(numbers, 5))
    process2 = multiprocessing.Process(target=add_number, args=(numbers, 10))

    # Iniciando os processos
    process1.start()
    process2.start()

    # Esperando os processos terminarem
    process1.join()
    process2.join()

    # Exibindo a lista após a execução dos processos
    print(numbers)
    
"""
Neste exemplo, 
estamos criando uma lista compartilhada chamada `numbers`
usando `multiprocessing.Manager().list()`. 

Em seguida, 
criamos dois processos que irão chamar a função `add_number` 
passando a lista compartilhada e um número para adicionar a essa lista. 

Ao final, 
imprimimos a lista para verificar que os dois processos de fato compartilharam a mesma lista.
"""