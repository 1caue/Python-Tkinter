from tkinter import *

def bt_click():
    print("Olá!")

    lb["text"] = "Funcionou!"


janela = Tk()

bt = Button(janela, width=20, text="ok", command=bt_click)
bt.place(x=100, y=100)

lb = Label(janela, text="Teste")
lb.place(x=100, y=150)

janela.geometry("300x400+200+200")
janela.mainloop()
