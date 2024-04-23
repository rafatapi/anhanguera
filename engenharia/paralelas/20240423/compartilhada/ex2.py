import threading
import multiprocessing

def incrementar(param_variavel):
	param_variavel.value += 1

variavel_compartilhada = multiprocessing.Value('i', 0)  # 'i' representa um inteiro
threads = []
for _ in range(10):
	thread = threading.Thread(target=incrementar, args=(variavel_compartilhada,))
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()

print(variavel_compartilhada.value)  # Output: 10
