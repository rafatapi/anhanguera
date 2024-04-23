from mpi4py import MPI
import numpy as np


# Inicialização dos processos de comunicação MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print("----------------------------------")
print(f"iniciando : {rank+1}/{size}")
print("----------------------------------")

# Definindo o tamanho do array
N = 100
array = np.arange(N)

# Dividindo o array entre os processos
local_array = np.zeros(N//size, dtype=int)  # Inicializa um array local vazio para cada processo

print(f"Processo {rank} antes do Scatter - local_array inicial:", local_array)

comm.Scatter(array, local_array, root=0)  # Divide o array original entre os processos
# Quando a função `comm.Scatter` é chamada, 
# o array original é dividido entre todos os processos. 
# Cada processo recebe uma parte do array, 
# de acordo com a divisão especificada pela divisão igual do array original. 
# Isso é útil em situações em que você deseja distribuir grandes conjuntos de dados 
# ou tarefas entre os processos para processamento paralelo.

print(f"Processo {rank} depois o Scatter - local_array recebido:", local_array)

# Realizando a soma localmente
local_sum = np.sum(local_array)  # Calcula a soma dos elementos no array local

print(f"Processo {rank} - Soma local:", local_sum)

# Reduzindo as somas locais para obter a soma total
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)  # Reduz as somas locais para o processo raiz

if rank == 0:
    print("Array original:", array)  # Imprime o array original
    print("Soma total:", total_sum)  # Imprime a soma total calculada


"""
Este programa é um exemplo de como utilizar o MPI (Message Passing Interface) em 
Python com a biblioteca mpi4py para distribuir a computação entre vários processos.

Aqui está uma explicação passo a passo do funcionamento do programa:

1. Importação das bibliotecas: 
	O programa começa importando as bibliotecas necessárias, `MPI` para comunicação 
	entre processos e `numpy` (abreviada como `np`) para operações numéricas.

2. Definição de comunicação: 
	É criado um comunicador MPI (`comm`) para gerenciar a comunicação entre os processos. 
	Em seguida, são obtidos o número de processo em execução (`rank`) 
	e o número total de processos no comunicador (`size`).

3. Definição do array: 
	Um array NumPy de tamanho 10 (variável `N`) 
	é criado com valores de 0 a 9 (array = np.arange(10)).

4. Divisão do array entre os processos: 
	O array é dividido igualmente entre os processos usando a função `Scatter` do MPI. 
	Cada processo recebe uma parte do array, armazenada em `local_array`, 
	que é um array NumPy local para cada processo.

5. Soma local: 
	Cada processo calcula a soma dos elementos em seu `local_array` 
	usando a função `np.sum()` e armazena o resultado em `local_sum`.

6. Reduzindo as somas locais: 
	Por fim, as somas locais de cada processo são reduzidas para obter a 
	soma total de todos os elementos do array. 
	Isso é feito com a função `reduce` do MPI, especificando a operação de 
	redução como a soma (`MPI.SUM`) e o processo raiz como o processo 0.

7. Saída dos resultados: 
	Se o processo em execução for o processo raiz (rank = 0), 
	ele imprime o array original e a soma total calculada.

Em resumo, o programa distribui um array entre vários processos, calcula a 
soma dos elementos localmente em cada processo e, em seguida, reduz essas somas 
locais para obter a soma total de todos os elementos do array. 
O MPI é utilizado para realizar a comunicação e coordenação entre os processos.
"""
