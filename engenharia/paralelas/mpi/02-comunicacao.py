### Comunicação Entre Processos
# Neste exemplo, mostramos uma simples comunicação ponto-a-ponto (send/receive).


from mpi4py import MPI

# Inicializa o ambiente MPI e obtém o comunicador global (COMM_WORLD)
comm = MPI.COMM_WORLD
# Obtém o rank (ID) do processo atual
rank = comm.Get_rank()

# Processo com rank 0 envia uma mensagem
if rank == 0:
    # Dados a serem enviados
    data = "Olá do processo 0"
    # Envia a mensagem para o processo com rank 1
    comm.send(data, dest=1, tag=11)
    print(f"[Processo {rank}] Enviou mensagem: {data} para o processo 1")

# Processo com rank 1 recebe a mensagem
elif rank == 1:
    # Recebe a mensagem do processo com rank 0
    data = comm.recv(source=0, tag=11)
    print(f"[Processo {rank}] Recebeu mensagem: {data} do processo 0")


# mpiexec -n 2 python D:\git-test\engenharia\paralelas\mpi\02-comunicacao.py