from xmlrpc.client import ServerProxy

proxy = ServerProxy('http://localhost:8000')
result_add = proxy.add(5, 3)
result_subtract = proxy.subtract(5, 3)

print("Resultado da adição:", result_add)
print("Resultado da subtração:", result_subtract)