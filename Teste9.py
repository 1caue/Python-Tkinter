from tkinter import *

janela = Tk()

lb1 = Label(janela, text="SIDE1", bg="blue")
lb2 = Label(janela, text="SIDE2", bg="grey")
lb3 = Label(janela, text="ANCHOR1", bg="blue")
lb4 = Label(janela, text="ANCHOR2", bg="grey")

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(anchor=NW)
lb4.pack(side=BOTTOM, anchor=SW)

janela["bg"] = "black"
janela.geometry("400x300+200+200")
janela.mainloop()
