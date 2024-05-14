# ------------------------------------------------------------------------------------
# 1. Importação das bibliotecas: 
#	O programa começa importando as bibliotecas necessárias, `MPI` para comunicação 
#	entre processos e `numpy` (abreviada como `np`) para operações numéricas.
# ------------------------------------------------------------------------------------
from mpi4py import MPI
import numpy as np

# ------------------------------------------------------------------------------------
# 2. Definição de comunicação: 
# 	É criado um comunicador MPI (`comm`) para gerenciar a comunicação entre os processos. 
# 	Em seguida, são obtidos o número de processo em execução (`rank`) 
# 	e o número total de processos no comunicador (`size`).
# ------------------------------------------------------------------------------------
# Inicialização dos processos de comunicação MPI
print("-----------------------------------------------------------------------------")
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# ------------------------------------------------------------------------------------
# 3. Definição do array: 
# 	Um array NumPy de tamanho 100 (variável `N`) 
# 	é criado com valores de 0 a 99 (array = np.arange(100)).
# ------------------------------------------------------------------------------------
# Definindo o tamanho do array
print("-----------------------------------------------------------------------------")
N = 100
array = np.arange(N)
print(f"Array original: {array}")

# ------------------------------------------------------------------------------------
# 4. Divisão do array entre os processos: 
# 	O array é dividido igualmente entre os processos usando a função `Scatter` do MPI. 
# 	Cada processo recebe uma parte do array, armazenada em `local_array`, 
# 	que é um array NumPy local para cada processo.
# ------------------------------------------------------------------------------------
# Dividindo o array entre os processos
print("-----------------------------------------------------------------------------")
local_array = np.zeros(N//size, dtype=int)  # Inicializa um array local vazio para cada processo
comm.Scatter(array, local_array, root=0)  # Divide o array original entre os processos
print(f"Array local do processo {rank}: {local_array}")

# ------------------------------------------------------------------------------------
# 5. Soma local: 
# 	Cada processo calcula a soma dos elementos em seu `local_array` 
# 	usando a função `np.sum()` e armazena o resultado em `local_sum`.
# ------------------------------------------------------------------------------------
# Realizando a soma localmente
print("-----------------------------------------------------------------------------")
local_sum = np.sum(local_array)  # Calcula a soma dos elementos no array local
print(f"Soma local do processo {rank}: {local_sum}")

# ------------------------------------------------------------------------------------
# 6. Reduzindo as somas locais: 
# 	Por fim, as somas locais de cada processo são reduzidas para obter a 
# 	soma total de todos os elementos do array. 
# 	Isso é feito com a função `reduce` do MPI, especificando a operação de 
# 	redução como a soma (`MPI.SUM`) e o processo raiz como o processo 0.
# ------------------------------------------------------------------------------------
# Reduz as somas locais para o processo raiz
print("-----------------------------------------------------------------------------")
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0) 
print(f"Soma total apos a reducao: {total_sum}")

# ------------------------------------------------------------------------------------
# 7. Saída dos resultados: 
# 	Se o processo em execução for o processo raiz (rank = 0), 
# 	ele imprime o array original e a soma total calculada.
# ------------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------")
if rank == 0:
    print("Array original:", array)  # Imprime o array original
    print("Soma total:", total_sum)  # Imprime a soma total calculada


print("-----------------------------------------------------------------------------")
# ------------------------------------------------------------------------------------
# Em resumo, o programa distribui um array entre vários processos, calcula a 
# soma dos elementos localmente em cada processo e, em seguida, reduz essas somas 
# locais para obter a soma total de todos os elementos do array. 
# O MPI é utilizado para realizar a comunicação e coordenação entre os processos.
# ------------------------------------------------------------------------------------



# mpiexec -n 2 python D:\git-test\engenharia\paralelas\mpi\mpi-1.py