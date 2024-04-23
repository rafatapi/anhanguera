import threading
import time

class ControleAeroporto:
    def __init__(self):
        self.mutex = threading.Lock()  # Mutex para controlar o acesso à pista

    def enter(self, voo, tempo_decolagem):
        self.mutex.acquire()  # Adquire o mutex para controle de acesso à pista
        print(f"{voo} usando a pista por {tempo_decolagem} segundos.")

    def exit(self, voo):
        print(f"{voo} liberando a pista.")
        self.mutex.release()  # Libera o mutex

def pista_controle(aeroporto, voo, tempo_decolagem):
    aeroporto.enter(voo, tempo_decolagem)  # Solicita acesso à pista
    time.sleep(tempo_decolagem)  # Simula o tempo de decolagem
    aeroporto.exit(voo)  # Informa que o voo liberou a pista

aeroporto = ControleAeroporto()  # Criando um controle de aeroporto com 1 pista
voos = [("AA123", 5), ("BA456", 7), ("DL789", 4), ("UA321", 3), ("LH654", 6), 
        ("AF987", 8), ("QF246", 5), ("EY555", 4), ("EK777", 7), ("SQ333", 6)]

# Criando threads para controlar os voos
threads = []
for voo, tempo_decolagem in voos:
    thread = threading.Thread(target=pista_controle, args=(aeroporto, voo, tempo_decolagem))
    threads.append(thread)
    thread.start()

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

print("Todos os voos decolaram.")