# Servidor
import Pyro4

@Pyro4.expose
class Calculadora:
	def soma(self, a, b):
		return a + b
	def subtracao(self, a, b):
		return a - b

daemon = Pyro4.Daemon()
uri = daemon.register(Calculadora)
print("URI do objeto remoto:", uri)
daemon.requestLoop()
