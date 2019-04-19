#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__      = 'Gabriel Gregório da Silva'
__email__       = 'gabriel.gregorio.1@outlook.com'
__description__ = 'Paleta de cores em poucas linhas!'
__status__      = 'Development'
__date__        = '19/04/2019'
__update__      = '19/04/2019'
__version__     = '1.0'

# Paleta de cores usada
__site__        = 'https://flatuicolors.com/palette/de'
__design__      = 'https://dribbble.com/srioz'

try:
    from tkinter import *
except:
    from Tkinter import *

tela = Tk()
tela.title('Paleta de cores')
tela.geometry('450x400+100+100')

x=0            # Andante pela horizontal
y=0            # Andante pela vertical
cor = 0        # Andante pela lista
vertical = 4   # Quantidade de blocos na vertical
horizontal = 5 # Quantidade de blocos na horizontal

# Cores que vão aparecer, linha por linha
lista = ['#fc5c65','#fd9644','#fed330','#26de81','#2bcbba','#eb3b5a','#fa8231','#f7b731','#20bf6b','#0fb9b1','#45aaf2','#4b7bec','#a55eea','#d1d8e0','#778ca3','#2d98da','#3867d6','#8854d0','#a5b1c2','#4b6584']

# Variável que permite a desseleção de um botão
global desselecionar

def clique(btn):
	# 
    global desselecionar
    try:
    	# Tentativa de mudar a cor da 'borda' do botão anterior que chamou o evento click, fazendo ele receber a cor de fundo dele mesmo
        desselecionar.configure(highlightbackground = desselecionar['bg'])
    except:
    	print("primeiro click!")
    desselecionar = btn # Registrar novo botão que chamou o evento click

    # Configurações estéticas
    print(btn['text'])
    btn['highlightbackground'] = 'white'

while y<vertical:
    # Fazer o botão oculpar as laterais.
    tela.grid_columnconfigure(x,weight=1)
    tela.rowconfigure(y,weight=1)

    # Tratamento de erro em caso de incidentes
    try:
    	lista[cor]
    except:
    	print('A lista de cores estorou! Vou reiniciar a variável cor para 0!')
    	cor = 0

    # Criação do botão.
    btn = Button(tela,bg=lista[cor],fg = 'white',activebackground=lista[cor],activeforeground='white',text = lista[cor],font=('Arial',11),relief=FLAT,highlightthickness=3,highlightbackground=lista[cor])
    btn['command'] = lambda btn=btn: clique(btn)
    btn.grid(row=y,column=x,sticky=NSEW)

    # Condicionais de controle
    x=x+1
    if x == horizontal:
        x=0
        y=y+1
    cor = cor+1

tela.mainloop()
