"""
Neste exemplo, vamos utilizar a memória compartilhada para que diferentes processos 
possam acessar e atualizar uma lista de tarefas de forma concorrente.
"""

# Importando as bibliotecas necessárias
import multiprocessing
import time

# Função para processar uma tarefa
def process_task(task, shared_list):
    time.sleep(5)  # Simula um processamento demorado
    result = f"Processando a tarefa: {task}"
    shared_list.append(result)

if __name__ == '__main__':
    tasks = ["Tarefa 1", "Tarefa 2", "Tarefa 3"]
    shared_list = multiprocessing.Manager().list()

    processes = []
    for task in tasks:
        p = multiprocessing.Process(target=process_task, args=(task, shared_list))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    for result in shared_list:
        print(result)


"""
Neste exemplo, criamos uma lista compartilhada utilizando `multiprocessing.Manager().list()` 
para armazenar os resultados do processamento de cada tarefa. Em seguida, criamos processos 
para processar cada tarefa, passando a lista compartilhada como argumento para que eles possam 
adicionar o resultado do processamento.

Após a execução dos processos, exibimos os resultados do processamento das tarefas. 
Este exemplo ilustra como a memória compartilhada pode ser útil para compartilhar dados entre 
processos e executar operações de forma concorrente, como no caso de processamento paralelo de tarefas.
"""