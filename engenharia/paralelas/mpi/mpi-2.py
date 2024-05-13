from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Definindo o número total de pontos
N = 1000000

# Gerando pontos aleatórios dentro do quadrado [0,1]x[0,1]
np.random.seed(rank)  # Seed diferente para cada processo
points = np.random.rand(N, 2)

# Contando quantos pontos estão dentro do círculo de raio 1
count = np.sum(np.linalg.norm(points, axis=1) < 1)

# Reduzindo a contagem de pontos dentro do círculo entre todos os processos
total_count = comm.reduce(count, op=MPI.SUM, root=0)

if rank == 0:
	pi_estimate = 4 * total_count / (N * size)
	print("Estimativa de Pi:", pi_estimate)
