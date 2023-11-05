from tkinter import *

janela = Tk()

lb1 = Label(janela, text="espaço", width="15", height=3, bg="green")
lbHORIZONTAL = Label(janela, text="Horizontal", bg="grey")
lbVERTICAL = Label(janela, text="Vertical", bg="grey")

lb1.grid(row=0, column=0)
lbHORIZONTAL.grid(row=1, column=0, sticky=E)
lbVERTICAL.grid(row=0, column=1, sticky=N)


janela.geometry("200x100+100+100")

janela.mainloop()
