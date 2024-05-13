import multiprocessing
import random

def sortear_numero(numeros_sorteados, id_thread, numero_sorteado_processo):
    # Sorteia um número aleatório entre 1 e 60
    numero_sorteado = random.randint(1, 60)
    
    while True:
        # Verifica se o número já foi sorteado anteriormente
        if numero_sorteado not in numeros_sorteados:
            numeros_sorteados[id_thread] = numero_sorteado
            numero_sorteado_processo.value = numero_sorteado
            break
        else:
            # Se o número já foi sorteado, sorteia novamente
            numero_sorteado = random.randint(1, 60)

if __name__ == "__main__":
    resultado = multiprocessing.Array('i', range(6))  # Array compartilhado para armazenar os números sorteados
    processos = []

    # Criar processos para sortear os números
    for i in range(6):
        numero_sorteado_processo = multiprocessing.Value('i', 0)  # Valor compartilhado para armazenar o número sorteado
        p = multiprocessing.Process(target=sortear_numero, args=(resultado, i, numero_sorteado_processo))
        p.start()
        processos.append(p)

    # Aguardar a finalização dos processos
    for p in processos:
        p.join()

    # Obter os números sorteados e exibí-los ordenadamente
    numeros_ganhadores = sorted([n for n in resultado])
    print("Números:", numeros_ganhadores)