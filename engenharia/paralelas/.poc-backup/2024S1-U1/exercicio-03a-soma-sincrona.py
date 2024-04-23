import time

# Lista de entradas para as somas
entradas = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9)]

# Função para somar dois números de forma assíncrona
def somar(x: int, y: int) -> int:
    time.sleep(1)
    return x + y

# Função para executar e exibir os resultados das somas assíncronas
def obter_resultados():

    # Cria uma lista de corrotinas para cada soma
    for v1,v2 in entradas:
        print(f"O resultado da soma é: {somar(v1,v2)}")

# Executa a função 'obter_resultados'
inicio = time.time()
obter_resultados()
print(f"Finalizado em {time.time() - inicio} segundos") 

