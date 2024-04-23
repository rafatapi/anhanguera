import asyncio
import time

# Lista de entradas para as somas
entradas = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9)]

# Função para somar dois números de forma assíncrona
async def somar(x: int, y: int) -> int:
    await asyncio.sleep(1)
    return x + y

# Função para executar e exibir os resultados das somas assíncronas
async def obter_resultados():

    # Cria uma lista de corrotinas para cada soma
    lista_processos = []
    for v1,v2 in entradas:
        lista_processos.append(somar(v1,v2))

    # Processa os resultados dos processos conforme eles finalizam
    for resposta in asyncio.as_completed(lista_processos):
        resultado = await resposta
        print(f"O resultado da soma é: {resultado}")

# Executa a função 'obter_resultados' utilizando o loop de eventos do asyncio
inicio = time.time()
asyncio.run(obter_resultados())
print(f"Tempo total: {time.time() - inicio} segundos")