import random
import multiprocessing

# Função que será executada pelos processos para contabilizar os votos
def count_votes(shared_dict, candidate):
    shared_dict[candidate] += 1

# Função para sortear um candidato aleatoriamente
def sortear_candidato(candidates):
    return random.choice(candidates)


if __name__ == '__main__':
    # Candidatos participantes da eleição
    candidates = ["Candidato A", "Candidato B", "Candidato C"]

    # Criando um dicionário compartilhado para armazenar os votos de cada candidato
    contagem = multiprocessing.Manager().dict({"Candidato A": 0, "Candidato B": 0, "Candidato C": 0})

    # Simulando os votos dos eleitores
    votos = []
    for _ in range(100):
        votos.append(sortear_candidato(candidates))

    # Criando os processos para contabilizar os votos
    processos = []
    for vote in votos:
        p = multiprocessing.Process(target=count_votes, args=(contagem, vote))
        p.start()
        processos.append(p)

    # Esperando os processos terminarem
    for p in processos:
        p.join()

    # Exibindo o total de votos de cada candidato após a execução dos processos
    for candidate, votos in contagem.items():
        print(f"{candidate}: {votos} votos")

