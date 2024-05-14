### Sincronização e Compartilhamento de Dados
# Neste exemplo, sincronizamos os processos usando `Barrier` e compartilhamos uma soma.

from mpi4py import MPI

# Inicializando o comunicador MPI padrão
comm = MPI.COMM_WORLD

# Obtendo o rank do processo atual
rank = comm.Get_rank()

# Cada processo vai calcular um valor baseado no seu rank (apenas para exemplo)
value = rank + 10  

# Sincronizando todos os processos no ponto de barreira
comm.Barrier()

# O valor de cada processo é reduzido ao somatório global na raiz (rank 0)
sum_value = comm.reduce(value, op=MPI.SUM, root=0)

# Apenas o processo com rank 0 imprime a soma total
if rank == 0:
    print(f"Soma total: {sum_value}")


# mpiexec -n 2 python D:\git-test\engenharia\paralelas\mpi\03-sincronizacao.py