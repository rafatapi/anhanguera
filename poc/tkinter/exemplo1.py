import tkinter as tk

root = tk.Tk()
def mostrar_mensagem():
    label.config(text="Olá, mundo!")

button = tk.Button(root, text="Clique aqui", command=mostrar_mensagem)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()