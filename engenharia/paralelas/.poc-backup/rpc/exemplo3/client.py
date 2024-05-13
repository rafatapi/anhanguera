# Cliente
import Pyro4

uri = input("Informe a URI do objeto remoto:")
calculadora = Pyro4.Proxy(uri)
num1 = 100
num2 = 50
resultado_soma = calculadora.soma(num1, num2)
resultado_subtracao = calculadora.subtracao(num1, num2)
print(f"A soma de {num1} e {num2} é: {resultado_soma}")
print(f"A subtração de {num1} por {num2} é: {resultado_subtracao}")

