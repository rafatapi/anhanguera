# Exemplo de variável compartilhada usando multiprocessing.Value
from multiprocessing import Value

shared_value = Value('i', 0)  # 'i' representa um inteiro

def incrementar():
    shared_value.value += 1

incrementar()
print(shared_value.value)  # Output: 1
