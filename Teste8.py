from tkinter import *

janela = Tk()

# Declarando os labels
lb1 = Label(janela, text="Label 1", bg="green")
lb2 = Label(janela, text="Label 2", bg="yellow")
lb3 = Label(janela, text="Label 3", bg="red")
lb4 = Label(janela, text="Label 4", bg="blue")
lb5 = Label(janela, text="Gerenciador de Leiaute", bg="white")

# Definindo o lado das labels 
lb1.pack(side=TOP)
lb2.pack(side=LEFT)     
lb3.pack(side=RIGHT)
lb4.pack(side=BOTTOM)
lb5.place(x=130, y=150)

janela["bg"] = "grey"
janela.geometry("400x300+200+200")
janela.mainloop()
