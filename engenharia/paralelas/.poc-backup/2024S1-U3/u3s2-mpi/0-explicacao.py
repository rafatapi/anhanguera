# https://acervolima.com/mpi-computacao-distribuida-facilitada/

"""
MPI (Message Passing Interface) é um padrão de comunicação usado em sistemas distribuídos e paralelos 
para permitir que processos diferentes possam trocar mensagens entre si. 
Ele fornece um conjunto de rotinas e bibliotecas que permitem a comunicação entre os processos de forma eficiente.

Em MPI, os processos são identificados por um número único chamado "rank" e 
podem enviar mensagens entre si utilizando funções de envio e recebimento.

Aqui está um exemplo prático em Python usando a biblioteca `mpi4py`, 
que implementa o padrão MPI:

1. Instale a biblioteca `mpi4py`:

```bash
pip install mpi4py
```

2. Criar um exemplo de programa em Python usando MPI:

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'msg': 'Hello, world!'}
    comm.send(data, dest=1)
elif rank == 1:
    data = comm.recv(source=0)
    print("Processo 1 recebeu a seguinte mensagem:", data)
```

Para executar o exemplo acima, você precisa ter acesso a um cluster com MPI instalado. 
Você pode executar o programa usando o comando `mpiexec` da seguinte forma:

```bash
mpiexec -n 2 python exemplo.py
```

Neste exemplo, dois processos MPI são iniciados e o processo com rank 0 envia 
uma mensagem para o processo com rank 1, que então imprime a mensagem recebida.

Espero que essa explicação básica e exemplo prático tenham sido úteis. 
Se precisar de mais informações, não hesite em perguntar.
"""