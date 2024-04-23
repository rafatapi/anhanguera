# https://blog.4linux.com.br/filas-assincronas-com-celery-e-redis/


#curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
#echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
#sudo apt-get update
#sudo apt-get install redis

from celery import Celery
import time

# Configura o Celery
app = Celery('tasks', broker='redis://localhost:6379/0')

# Define a tarefa `running` usando o decorador `@app.task`
@app.task
def running(runner, vel):
    """
    Tarefa `running` que simula um corredor correndo a uma determinada velocidade.

    Args:
        runner (str): Nome do corredor.
        vel (int): Velocidade do corredor em metros por segundo.
    """

    distancia = 0  # Define a distância inicial como 0 metros
    while True:  # Loop infinito para simular a corrida contínua
        time.sleep(2)  # Aguarda 2 segundos para simular a passagem do tempo
        distancia += vel  # Atualiza a distância percorrida
        print(f"Corredor {runner} está em {distancia} metros.")  # Imprime a distância atual

# Ao executar este código, a tarefa `running` não será executada automaticamente.
# É necessário utilizar ferramentas como o `celery -A tasks worker` para iniciar um worker
# do Celery que ficará responsável por processar as tarefas enfileiradas.
        
#from tasks import running

#running.delay('Tiago Assunção', 3)
#running.delay('Leonardo Bites', 4)
#running.delay('Silvia Mendes', 5)