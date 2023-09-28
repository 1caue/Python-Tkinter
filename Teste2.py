# Importando o módulo ↓
import tkinter as tk 

# Definindo a varivel ↓
janela = tk.Tk()

# Definindo o titulo da aba
janela.title("Ead Ouro Moderno")

# Definindo cor de fundo
janela["bg"] = "grey"

# Definindo o tamanho da tela (Largura x Altura 
# + Distancia da margem esquerda + Distancido topo do video) ↓
janela.geometry('800x800+100+100')

# Executando ↓
janela.mainloop()

