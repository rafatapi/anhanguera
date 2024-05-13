import multiprocessing

# Função para calcular a média de uma lista de números
def calcular_media(soma_compartilhada, contagem_compartilhada, numeros_parte):
    soma_local = 0
    contagem_local = 0

    # Calcular a soma e a contagem dos números na lista
    for lista_numeros in numeros_parte:
        for num in lista_numeros:
            soma_local += num
            contagem_local += 1

    print(f"Processo {multiprocessing.current_process().pid}: Soma local = {soma_local}, Contagem = {contagem_local}")

    # Atualizar os valores compartilhados
    soma_compartilhada.value += soma_local
    contagem_compartilhada.value += contagem_local

if __name__ == "__main__":
    numeros = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    # Variáveis compartilhadas para armazenar a soma total e a contagem de números
    soma_compartilhada = multiprocessing.Value('d', 0.0)  # 'd' indica um double (número decimal)
    contagem_compartilhada = multiprocessing.Value('i', 0)  # 'i' indica um inteiro

    processos = []

    # Criar um processo para cada lista de números
    for sub_lista in numeros:
        p = multiprocessing.Process(target=calcular_media, args=(soma_compartilhada, contagem_compartilhada, [sub_lista]))
        p.start()
        processos.append(p)

    for p in processos:
        p.join()

    # Calcular a média final
    media = soma_compartilhada.value / contagem_compartilhada.value
    print(f"A média dos números é: {media:.2f}")