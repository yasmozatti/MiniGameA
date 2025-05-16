import tkinter
from tkinter import *
from tkinter import ttk

# Cores
co0 = "#444466" #Preto
co1 = "#feffff" #Banco
co2 = "#66CCFF" #Azul
co3 = "#000066" #Valoir
co4 = "#003300" #Letra
co5 = "#e06636" #- profit
co6 = "#6dd695" #+ profit
co7 = "#ef5350" # Vermelha
co8 = "#00bfa5" #Verde
fundo = "#3b3b3b"
co10 = "#fcfbf7"

cor1 = "#f58b5d"
cor2 = "#ff333a"
cor3 = "#6bd66f"
cor4 = "#ab8918"

janela = Tk()
janela.title('')
janela.geometry('350x280')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=2, ipadx=200)

frame_top = Frame(janela, width=350, height=30, bg=co1, pady=0, padx=0, relief='flat')
frame_top.grid(row=1, column=0, sticky=NW)
frame_corpo= Frame(janela, width=350, height=200, bg=fundo, pady=0,padx=0, relief='flat')
frame_corpo.grid(row=2, column=0, sticky=NW)

style = ttk.Style(janela)
style.theme_use("clam")

#Configurando do frame top
app_nome = Label(frame_top, text="ADIVINHE O NÚMERO", anchor='center', font=('verdana 14 bold'), bg=co1, fg=co3)
app_nome.place(x=55,y=0)

# Configurando o frame_bottom
l_pontos = Label(frame_corpo, text ='Prontuação = 0', anchor='center', font=('Ivy 11 bold'), bg=fundo, fg=co1)
l_pontos.place(x=40, y=30)
l_tentativas = Label(frame_corpo, text='Tentativas 5', anchor='center', font=('Ivy 11 bold'), bg= fundo, fg=co1)
l_tentativas.place(x=205, y=30)

l_linha = Label(frame_corpo, text='', width='90',anchor='center', font=('Ivy 4'), bg=co3, fg=co1)
l_linha.place(x=39, y=59)

l_regra_1 = Label(frame_corpo, text ='Tente adivinhar o número para pontuar', anchor='center', font=('Ivy 8 bold'), bg= fundo, fg=co1)
l_regra_1.place(x=40, y=80)



janela.mainloop()