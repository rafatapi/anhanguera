### Empacotamento de Dados Paralelo
# Neste exemplo, dividimos um vetor grande em pedaços menores e processamos cada pedaço em paralelo.

from mpi4py import MPI
import numpy as np

# Inicialização do ambiente MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # Identifica o rank (ID) do processo atual
size = comm.Get_size()  # Obtém o número total de processos

# Define o tamanho do vetor
N = 100

# O processo com rank 0 inicializa o vetor de dados
if rank == 0:
    data = np.arange(N, dtype='i')
else:
    data = None

# Exibe os dados iniciais em cada processo
print(f"[Processo {rank}] Dados iniciais: {data}")

# Cada processo aloca espaço para sua porção dos dados
local_data = np.zeros(N // size, dtype='i')

# Scatter distribui partes do vetor 'data' para todos os processos
comm.Scatter(data, local_data, root=0)

# Cada processo dobra seus dados locais
local_data = local_data * 2

# Buffer para reunir os dados processados (no processo root)
gathered_data = None
if rank == 0:
    gathered_data = np.empty(N, dtype='i')

# Gather reúne os dados processados em 'gathered_data' no processo root
comm.Gather(local_data, gathered_data, root=0)

# O processo root exibe os dados finais e calcula a soma
if rank == 0:
    print(f"[Processo {rank}] Dados finais: {gathered_data}")
    
    # Calculando a soma total dos dados processados
    total_sum = np.sum(gathered_data)
    print(f"[Processo {rank}] Soma total dos dados: {total_sum}")
else:
    print(f"[Processo {rank}] Enviou dados processados para o processo 0")


# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

# mpiexec -n 2 python D:\git-test\engenharia\paralelas\mpi\01-empacotamento.py
