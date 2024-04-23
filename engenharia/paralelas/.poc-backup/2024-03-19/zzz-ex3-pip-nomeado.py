import threading

def producer():
    for i in range(10):
        message = f"Mensagem {i}"
        print(f"Produtor enviando: {message}")
        with open('pipe', 'w') as pipe:
            pipe.write(message + '\n')

def consumer():
    with open('pipe', 'r') as pipe:
        for line in pipe:
            message = line.strip()
            print(f"Consumidor recebendo: {message}")

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


"""
Explicação:

    Este código usa um pipe nomeado chamado 'pipe' para comunicação entre o produtor e o consumidor.
    O pipe é unidirecional, ou seja, o produtor só pode enviar mensagens para o consumidor.
    Os dados são gravados no pipe e lidos na mesma ordem (FIFO).

----------------------------------------------------------------------------------------------------
Explicação:

    Importação:
        import threading: Importa a biblioteca threading para criar threads.

    Funções:

        producer():
            Envia 10 mensagens para um pipe nomeado 'pipe'.
            Usa with open para abrir o pipe em modo de escrita ('w').
            Escreve cada mensagem no pipe e adiciona uma nova linha ('\n').
            Fecha o pipe automaticamente ao sair do bloco with.

        consumer():
            Lê mensagens do pipe nomeado 'pipe'.
            Usa with open para abrir o pipe em modo de leitura ('r').
            Lê cada linha do pipe e imprime a mensagem.
            Fecha o pipe automaticamente ao sair do bloco with.

    Execução:
        Cria duas threads: producer_thread e consumer_thread.
        Inicia as threads usando start().
        Aguarda a finalização das threads usando join().

Observações:

    Este código usa pipes nomeados para comunicação entre processos.
    Pipes são unidirecionais, ou seja, a comunicação é apenas de um processo para outro.
    Para comunicação bidirecional, você pode usar pipes aninhados ou sockets.

Aprimoramentos:

    Adicione verificação de erros para lidar com possíveis falhas de abertura do pipe.
    Implemente um mecanismo de sincronização para evitar que o consumidor leia mensagens antes de serem escritas pelo produtor.
    Utilize pipes aninhados para comunicação bidirecional entre os processos.


--------------------------------------
No contexto do código Python que forneci para a aula prática de passagem de mensagem entre processos, "pipe" se refere a um pipe nomeado do sistema operacional. É um mecanismo de comunicação unidirecional que permite a um processo gravar dados em um arquivo especial e outro processo ler esses dados do mesmo arquivo.

Aqui estão alguns detalhes adicionais sobre pipes nomeados:

    Criação: Um pipe nomeado é criado usando funções do sistema operacional específicas para cada plataforma (por exemplo, mkfifo no Linux/Unix).
    Unidirecional: Os pipes nomeados são unidirecionais, o que significa que os dados fluem apenas em uma direção - do processo gravador para o processo leitor.
    FIFO (First-In, First-Out): Os dados são lidos do pipe na mesma ordem em que foram gravados (similar a uma fila).
    Sem buffer: Os pipes nomeados não possuem buffer interno. O processo leitor precisa estar pronto para ler os dados assim que o processo gravador os escreve.

Vantagens:

    Simples de implementar.
    Adequado para comunicação entre processos relacionados (dentro do mesmo programa).

Desvantagens:

    Unidirecional: Não permite comunicação bidirecional entre processos.
    Sem buffer: Pode levar a perda de dados se o processo leitor não estiver pronto para ler os dados quando o processo gravador os escreve.
    Limitações de plataforma: A criação e utilização de pipes nomeados podem variar entre diferentes sistemas operacionais.

Alternativas:

    Pipes aninhados: Podem ser usados para criar comunicação bidirecional entre processos. Envolve a criação de dois pipes nomeados, um para cada direção da comunicação.
    Sockets: Fornecem um mecanismo de comunicação mais robusto e flexível entre processos, podendo ser bidirecionais e independentes do sistema operacional.

Conclusão:

Pipes nomeados são uma maneira simples de implementar a passagem de mensagens entre processos em Python, mas é importante entender suas limitações e considerar alternativas caso precise de funcionalidades mais avançadas como comunicação bidirecional ou suporte a diferentes sistemas operacionais.
"""