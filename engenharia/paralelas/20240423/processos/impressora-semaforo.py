import threading
import time

# Array com os nomes dos documentos
documentos = ["document1.doc", "planilha.xls", "apresentacao.ppt", "contrato.pdf", "foto.jpg", "relatorio.docx", "apostila.pdf", "planodesaude.xls", "apresentacao3.ppt", "proposta.pdf"]

# Semaforo para controlar o envio dos documentos para impressão
semaforo_impressao = threading.Semaphore(3)

class FilaImpressao(threading.Thread):
    def __init__(self, documento):
        super().__init__()
        self.documento = documento

    def run(self):
        print(f"Enviando o arquivo {self.documento} para impressão.")
        try:
            semaforo_impressao.acquire()
            
            print(f"Iniciando impressão do documento {self.documento}.")
            time.sleep(3)  # Simulação de tempo de impressão
            
            print(f"Documento {self.documento} impresso com sucesso!")
            
        finally:
            semaforo_impressao.release()
            print(f"{self.documento} pronto para ser retirado.")

# Criando e iniciando threads para os documentos
fila_impressao = []
for doc in documentos:
    fila_impressao.append(FilaImpressao(doc))

for impressao in fila_impressao:
    impressao.start()

# Aguardando o término de todas as threads
for impressao in fila_impressao:
    impressao.join()

print("Todos os documentos foram impressos.")