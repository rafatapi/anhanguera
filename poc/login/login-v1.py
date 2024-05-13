# Definindo as credenciais
usuario_cadastrado = "usuario123"
senha_cadastrada = "senha123"

# Pedindo as credenciais ao usuário
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Verificando se as credenciais estão corretas
if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print("Login bem sucedido!")
else:
    print("Credenciais incorretas. Tente novamente.")