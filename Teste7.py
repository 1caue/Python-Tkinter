from tkinter import *

def button():
    # Extraindo valores do Entry ↓
    print(ed.get())
    lb["text"] = ed.get()

janela = Tk()

# "Entry", ele irá inserir a barra para digitar ↓
ed = Entry(janela)
ed.place(x=100, y=100)

bt = Button(janela, width=20, text="Botão", command=button)
bt.place(x=99, y=120)

lb = Label(janela, text="Label")
lb.place(x=100, y=200)

janela.geometry("600x300+300+300")
janela.mainloop()
