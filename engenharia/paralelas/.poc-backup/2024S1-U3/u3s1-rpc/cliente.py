from xmlrpc.client import ServerProxy

# Conecta ao servidor RPC
server = ServerProxy('http://localhost:8000')

# Chama a função remota 'add' enviando os parâmetros 5 e 3
result_add = server.add(5, 3)
print("Resultado da chamada remota para 'add()':", result_add)

# Chama a função remota 'multiply' enviando os parâmetros 5 e 3
result_multiply = server.multiply(5, 3)
print("Resultado da chamada remota para 'multiply()':", result_multiply)