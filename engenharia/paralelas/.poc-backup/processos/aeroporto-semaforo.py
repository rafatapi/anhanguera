import threading
import time

class ControleAeroporto:
    def __init__(self, num_pistas):
        self.num_pistas = num_pistas
        self.pistas_disponiveis = [False] * num_pistas
        self.semaforo = threading.Semaphore(num_pistas)

    def enter(self, voo, tempo_decolagem):
        # Adquire o semáforo para controlar o acesso às pistas
        self.semaforo.acquire()
        
        # Itera sobre as pistas disponíveis para encontrar uma que esteja livre
        for i in range(self.num_pistas):
            if not self.pistas_disponiveis[i]:
                self.pistas_disponiveis[i] = True
                print(f"{voo} usando pista {i+1} por {tempo_decolagem} segundos.")
                return i

    def exit(self, voo, pista):
        # Marca a pista como disponível ao final do pouso
        self.pistas_disponiveis[pista] = False
        print(f"{voo} liberando pista {pista+1}")
        
        # Libera o semáforo, indicando que a pista está livre
        self.semaforo.release()

def pista_controle(aeroporto, voo, tempo_decolagem):
    # Solicita acesso a uma pista disponível
    pista = aeroporto.enter(voo, tempo_decolagem)
    
    # Simula o tempo de decolagem
    time.sleep(tempo_decolagem)
    
    # Informa que o voo liberou a pista após a decolagem
    aeroporto.exit(voo, pista)

aeroporto = ControleAeroporto(2)  # Criando um controle de aeroporto com 2 pistas
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