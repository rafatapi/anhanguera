from mpi4py import MPI

# Inicialização dos processos de comunicação MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


# Envio e recebimento de mensagens entre processos
if rank == 0:
    data = {'message': "Hello from process 0!"}
    comm.send(data, dest=1)  # Envia mensagem para o processo com rank 1
    print(f"Processo {rank} enviou mensagem para processo 1.")
elif rank == 1:
    data = comm.recv(source=0)  # Recebe mensagem do processo com rank 0
    print(f"Processo {rank} recebeu a seguinte mensagem: {data['message']}")
    

"""
Neste exemplo, o processo com rank 0 envia uma mensagem para o processo com rank 1 
utilizando a função `send`, e o processo com rank 1 recebe essa mensagem utilizando 
a função `recv`.

Ao rodar esse código com dois processos, o output esperado seria:

Processo 0 enviou mensagem para processo 1.
Processo 1 recebeu a seguinte mensagem: Hello from process 0!
"""	