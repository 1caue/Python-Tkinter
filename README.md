# Python-Tkinter
# Aprendizados e alguns testes usando a Biblioteca "tkinter" de Python

Bom, primeiramente teremos que importar a biblioteca tkinter usando o "from tkinter import *", usando esse metódo, importaremos toda a biblioteca tkinter, logo após isso, declararemos uma janela com a instância de tk, assim:

    janela = Tk() 

e em seguida criaremos um label vinculado a janela e o texto que o mesmo irá mostrar na tela, assim:

    Label(janela, text="Olá, Mundo!").pack()

o gerenciador ".pack()" utilizado no final da variavel tambem é utilizado. E por fim mandaremos nossa aplicação ser executada utilizadndo o ".mainloop()" assim:

    janela.mainloop()

E o código final ficará assim:

    from tkinter import * # O "*" importará toda a biblioteca
    
    janela = Tk()
    
    Label(janela, text='Olá Mundo!').pack()
    
    janela.mainloop()

---
		 
# DEFINIÇÕES	 

O nome Tkinter vem da expressão Tk Interface

- Tkinter é biblioteca gráfica nativa do Python

- Multiplataforma nos principais sistemas Unix e Microsoft Windows

- A biblioteca é um binding

GUI:
Frequentemente nós iremos ver e falar a palavra "GUI". 
G raphic
U ser
I nterface

Então todas as vezes que você ver a expressão GUI(Interface Grafica do Usuário), Você pode estar certo que o texto vai estar fazendo referência a alguma parte gráfica de alguma aplicação.

Widget:
Já o Widget é todo componente que compôem uma interface gráfica, ex:botôes de opção, campos de texto, janelas e rótulos de texto. 

Conteiner:
Conteiner é um widget que pode conter outros widgets. Todo conteiner também está contido em outro container, salvo a janela principal. Toda vez que estivemos falando de contêiner, nós vamos estar falando de alguma parte gráfica que é capaz de conter outra parte gráfica

Window:
Window é um termo que possui significados diferentes em contextos diferentes. Em geral, se refere a uma área retangular em algum lugar da tela de exibição.

Top-Level Window:
top-level window diz-se a uma janela independente e que normalmente esta sendo exibida sob as demais.

Frame:
frame é a unidade básica de organização de layout complexo. 
 
Chield-parent:
chield-parent é o nome da relação entre um widget e seu container. Um campo adicionado a uma janela é uma relação parent-chield, onde a janela é o parent e o campo o chield. 

---

# O código Minimo

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

---
	
# Os 3 pilares doDesevolvimento de aplicações gráficas

1) Gerenciadores de Leiaute
2) Widget (COMPONENTES DE TELA) 
3) Eventos 

---

# Gerenciador de layout	
 
Gerenciador de layout é um widget que gerencia o posicionamento dos componentes dentro de um contêiner. Todos os contêiners devem utilizar um gerenciador de layout para exibir os Widgets, e cada um deles possui uma caracteristica bem definida.

- Um gerenciador de layout define a organização dos widgets dentro de um container

OS 3 GERENCIADORES DE LAYOUT
place - os widgets são dispostos conforme suas coordenadas x e y

pack - empacota os widgets na horizontal ou vertical

grid - os widgets são inseridos num sistema de células de uma tabela

Place:
O gerenciador deleiaute place é o gerenciador que nos permite definir o lugar onde nós queremos o componente
