import threading
import time

class ControleAeroporto:
    def __init__(self):
        self.pista_disponivel = True  # Inicialmente a pista está disponível

    def enter(self, voo, tempo_decolagem):
        # Enquanto a pista estiver ocupada, o voo aguarda
        while not self.pista_disponivel:
            print(f"{voo} aguardando pista disponível.")
            time.sleep(1)
        
        self.pista_disponivel = False  # Marca a pista como ocupada
        print(f"{voo} usando a pista por {tempo_decolagem} segundos.")

    def exit(self, voo):
        self.pista_disponivel = True  # Marca a pista como disponível
        print(f"{voo} liberando a pista.")

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