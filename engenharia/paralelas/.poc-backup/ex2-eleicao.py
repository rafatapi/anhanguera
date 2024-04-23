import random
import multiprocessing

# Função para sortear um candidato aleatoriamente
def sortear_candidato(candidates):
    return random.choice(candidates)

# Função que será executada pelos processos para contabilizar os votos
def count_votes(shared_dict, candidate):
    shared_dict[candidate] += 1

if __name__ == "__main__":
    # Candidatos participantes da eleição
    candidates = ["Candidato A", "Candidato B", "Candidato C"]

    # Criando um dicionário compartilhado para armazenar os votos de cada candidato
    contagem = multiprocessing.Manager().dict({"Candidato A": 0, "Candidato B": 0, "Candidato C": 0})

    # Simulando os votos aleatórios dos eleitores
    votos = [sortear_candidato(candidates) for _ in range(100)]

    # Criando os processos para contabilizar os votos
    processos = [multiprocessing.Process(target=count_votes, args=(contagem, vote)) for vote in votos]
    [p.start() for p in processos]
    [p.join() for p in processos]

    # Exibindo o total de votos de cada candidato após a execução dos processos
    for candidate, votos in contagem.items():
        print(f"{candidate}: {votos} votos")