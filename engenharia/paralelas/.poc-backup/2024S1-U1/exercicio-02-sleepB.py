from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep, time

# Função que retorna após um tempo aleatório
def retornar_apos_5_segundos(num):
    sleep(num)
    return "  > retorno de {}".format(num)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
print(f"Assincrono com Thread :")
start = time()

# Criando um pool de threads com 5 threads
pool = ThreadPoolExecutor(5)
futuros = []

# Submetendo as tarefas ao pool de threads
for x in range(5):
    futuros.append(pool.submit(retornar_apos_5_segundos, x))

# Esperando as tarefas completarem e exibindo os resultados
for x in as_completed(futuros):
    print(x.result())
    
print(f"Tempo total: {time() - start} segundos")