from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Define a função que será chamada remotamente
def add(x, y):
    return x + y

# Função para multiplicar dois números
def multiply(x, y):
    return x * y


# Instancia um servidor RPC
server = SimpleXMLRPCServer(('localhost', 8000), requestHandler=SimpleXMLRPCRequestHandler)
server.register_introspection_functions()
server.register_function(add, 'add')
server.register_function(multiply, 'multiply')

# Inicia o servidor
print("Servidor RPC iniciado em http://localhost:8000/")
server.serve_forever()