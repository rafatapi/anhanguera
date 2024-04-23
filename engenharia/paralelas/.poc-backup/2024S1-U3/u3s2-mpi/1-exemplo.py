from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'msg': 'Hello, world!'}
    comm.send(data, dest=1)
elif rank == 1:
    data = comm.recv(source=0)
    print("Processo 1 recebeu a seguinte mensagem:", data)


# para executar
# mpiexec -n 2 python D:\git-gcp\paralelo\2024S1-U3\u3s2-mpi\exemplo.py