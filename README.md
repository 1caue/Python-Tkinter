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

Place
O gerenciador deleiaute place é o gerenciador que nos permite definir o lugar onde nós queremos o componente

---

# Gerenciador de Leiaute pack  

- PACK
A constante "Top" Representa a parte superior, a "Left" Representa o lado esquerdo, o "Right" Representa o lado direito e o "Bottom" representa a parte inferior
EX:

	  "side=TOP"

---

# Propiedade Side

Através da propiedade side definimos qual o lado que nós queremos posicionar o nosso componente 
Os principais argumentos que você pode usar com o pack são side (lado), fill (preenchimento), expand (expansão), e anchor (âncora). O argumento side define em qual lado do container o widget será colocado. O argumento fill especifica se o widget deve preencher o espaço alocado a ele, e expand determina se o widget deve se expandir para preencher qualquer espaço extra disponível. O argumento anchor controla como o widget é ancorado dentro do espaço alocado a ele.

---

# Propiedade anchor 

- A Propiedade anchor define os sentidos da mesma forma que está defininido numa bussola

![](![image](https://github.com/1caue/Python-Tkinter/assets/142410809/5cbac3d5-2bd5-46b3-9dcf-0b6327f62f33)

A propriedade anchor em tkinter é usada para definir a posição de um widget em relação ao ponto em que está localizado. 

Ela aceita valores como "n", "s", "e", "w" e suas combinações, representando os pontos cardeais (norte, sul, leste, oeste) e também combinações como "nw", "ne", "sw", "se" para diagonais. Isso ajuda a determinar a direção em que um widget se expande em seu contêiner. Por exemplo, se um widget tiver o valor de anchor definido como "center", ele ficará centralizado em relação ao ponto definido no contêiner. 

---

# Propiedade Fill

A utilização da propriedade fill em Tkinter está associada ao método pack, que é um dos gerenciadores de layout disponíveis nesta biblioteca. Se estiver utilizando outro gerenciador de layout, como grid ou place, a abordagem pode ser diferente. Certifique-se de ajustar a propriedade fill de acordo com o gerenciador de layout que estiver utilizando.

---

# Propiedade expand

- A propiedade expand não irá fazer com que os nossos widgets se expande mas sim fará com que eles tenham o mesmo tamanho

A propriedade "expand" em Python com a biblioteca tkinter é usada para especificar se um widget deve se expandir para preencher qualquer espaço extra no contêiner (normalmente um widget de um layout de grade) disponível para ele. Se definido como "True", o widget expandirá para preencher o espaço disponível.

---

# Gerenciador de leiaute Grid 

- Definimos a posição de cada widget com o método grid(), que recebe os parâmetros row e column, com a respectiva posição e numeração de cada linha e coluna.

O gerenciador de leiaute "grid" em tkinter é um método de organização de widgets em uma janela ou em um frame. Com esse gerenciador, você pode organizar os widgets em linhas e colunas, semelhante a uma tabela. Você pode especificar em qual linha e coluna um widget deve ser colocado e quantas linhas e colunas ele deve ocupar

---

# Propiedade Row e Columm (Linha e coluna)

As propriedades "row" e "column" em tkinter são usadas em conjunto com o gerenciador de leiaute "grid". Elas são usadas para posicionar um widget em uma determinada linha e coluna dentro de um contêiner, como uma janela ou um frame. Você pode atribuir valores inteiros a essas propriedades para especificar a posição de um widget. Por exemplo, se você definir "row=0" e "column=0" para um widget, ele será posicionado no canto superior esquerdo do contêiner. Com o gerenciador de leiaute "grid", você pode organizar os widgets em uma grade, determinando onde eles devem ser colocados em termos de linhas e colunas.

	from tkinter import * 
	
	janela = Tk()
	
	lb1 = Label(janela, text="Label 1")
	lb2 = Label(janela, text="Label 2")
	
	lb1.grid(row=1000, column=1000)
	lb2.grid(row=2000, column=2000)
	
	
	janela.geometry("1000x200+-600+200")
	
	janela.mainloop()

---

# Propriedade Sticky

Em Tkinter, a propriedade sticky é usada em conjunto com a propriedade grid para especificar em que direção um widget deve se expandir para preencher o espaço disponível dentro de uma célula de grade. A propriedade sticky aceita uma ou mais combinações de pontos cardeais (N, E, S, W) ou o ponto cardeal central (C) para indicar a direção de expansão. Aqui está como ela funciona:

- N: Norte (topo)
- S: Sul (base)
- E: Leste (direita)
- W: Oeste (esquerda)
- C: Central

Quando você define a propriedade sticky em um widget durante a chamada grid, o widget se expandirá na direção especificada para preencher o espaço alocado na célula da grade.

Ex: 

	lbHORIZONTAL.grid(row=1, column=0, sticky=E)
	lbVERTICAL.grid(row=0, column=1, sticky=N)

---

# Propiedade rowspan e columnspan

Quando você está organizando widgets em uma grade usando o gerenciador de layout grid do Tkinter, pode usar essas propriedades para especificar quantas linhas ou colunas adjacentes um widget deve ocupar.

Por exemplo, se você tem um widget que deve se estender por duas linhas e duas colunas, você pode definir rowspan=2 e columnspan=2 para esse widget.
