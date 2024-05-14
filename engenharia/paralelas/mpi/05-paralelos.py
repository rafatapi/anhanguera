### Desenvolvimento de Algoritmos Paralelos
# Neste exemplo, implementamos uma versão paralela do algoritmo de redução.

from mpi4py import MPI

# Inicializando o comunicador MPI padrão
comm = MPI.COMM_WORLD

# Obtendo o rank do processo atual
rank = comm.Get_rank()

# Obtendo o número total de processos
size = comm.Get_size()

# Cada processo define um valor diferente, baseado no seu rank
data = rank + 1

# Realizando a operação de redução allreduce para somar os valores de todos os processos
sum_data = comm.allreduce(data, op=MPI.SUM)

# Imprimindo a soma total em cada processo
print(f"Processo {rank} tem soma total: {sum_data}")


# mpiexec -n 2 python D:\git-test\engenharia\paralelas\mpi\05-paralelos.py