import asyncio
from time import time

# Função que retorna após um tempo aleatório
async def retornar_apos_5_segundos_async(num):
    await asyncio.sleep(num)
    return "  > retorno de {}".format(num)


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Função para executar e exibir os resultados das somas assíncronas
async def obter_resultados():

    # Cria uma lista de corrotinas para cada soma
    lista_processos = []
    for x in range(5):
        lista_processos.append(retornar_apos_5_segundos_async(x))

    print("lista de processos assincronos criados")

    # Processa os resultados dos processos conforme eles finalizam
    for resposta in asyncio.as_completed(lista_processos):
        resultado = await resposta
        print(f"{resultado}")


print(f"Assincrono com asyncio :")
start = time()
asyncio.run(obter_resultados())
print(f"Tempo total: {time() - start} segundos")
