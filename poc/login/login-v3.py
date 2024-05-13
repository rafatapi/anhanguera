import tkinter as tk
from tkinter import messagebox

def verificar_credenciais():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "usuario123" and senha == "senha123":
        messagebox.showinfo("Sucesso", "Login bem sucedido!")
    else:
        messagebox.showerror("Erro", "Credenciais incorretas. Tente novamente.")

# Criando a janela
janela = tk.Tk()
janela.title("Login")
janela.geometry("300x200")


# Criando os campos de entrada
label_usuario = tk.Label(janela, text="Usuário:", font=('Helvetica', 12))
label_usuario.pack()
entry_usuario = tk.Entry(janela, font=('Helvetica', 12))
entry_usuario.pack()

label_senha = tk.Label(janela, text="Senha:", font=('Helvetica', 12))
label_senha.pack()
entry_senha = tk.Entry(janela, show="*", font=('Helvetica', 12))
entry_senha.pack()

# Botão de login
botao_login = tk.Button(janela, text="Login", command=verificar_credenciais, font=('Helvetica', 12))
botao_login.pack()

# Rodando a janela
janela.mainloop()