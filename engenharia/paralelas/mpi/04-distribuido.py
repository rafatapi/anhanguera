### Processamento Distribuído de Tarefas
# Neste exemplo, distribuímos uma função de cálculo a ser executada em processos diferentes.

from mpi4py import MPI

def compute_square(rank):
    # Função que calcula o quadrado do rank do processo
    return rank * rank

# Inicializando o comunicador MPI padrão
comm = MPI.COMM_WORLD

# Obtendo o rank do processo atual
rank = comm.Get_rank()

# Obtendo o número total de processos
size = comm.Get_size()

# Cada processo calcula o quadrado do seu próprio rank
local_result = compute_square(rank)

# Reunindo os resultados de todos os processos no processo raiz (rank 0)
results = comm.gather(local_result, root=0)

# Apenas o processo com rank 0 imprime os resultados coletados
if rank == 0:
    print("Resultados:", results)

# mpiexec -n 2 python D:\git-test\engenharia\paralelas\mpi\04-distribuido.py

