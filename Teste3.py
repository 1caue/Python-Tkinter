from tkinter import *

janela = Tk()

Lb = Label(janela, text="Fala Galera!!!")
Lb.place(x=100, y=100)

# widgt x high + left + top
janela.geometry("300x300+200+200")

janela.mainloop()
