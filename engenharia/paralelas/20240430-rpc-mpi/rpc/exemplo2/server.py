# Servidor
from xmlrpc.server import SimpleXMLRPCServer

def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

server = SimpleXMLRPCServer(('localhost', 8000))
server.register_function(add_numbers, 'add')
server.register_function(subtract_numbers, 'subtract')

server.serve_forever()