from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep, time

# Função que retorna após um tempo aleatório
def retornar_apos_5_segundos(num):
    sleep(num)
    return "  > retorno de {}".format(num)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
print(f"Sincrono :")
start = time()
for x in range(5):
    print(retornar_apos_5_segundos(x))
print(f"Tempo total: {time() - start} segundos")


print("")   
