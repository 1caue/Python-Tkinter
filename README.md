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



