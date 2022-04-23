from tkinter import *
from math import *
from cmath import *
from random import *


janela = Tk() # janela
janela.geometry("700x500") # tamanho da janela
janela.title('CALCULADORA') # titulo

bot_r = Label(janela, text = "", background = "#A1A1A1")
bot_r.pack(ipadx = 20, ipady = 20, padx = 5, pady = 5, side = "top" , fill = X, expand = True)
janela.mainloop()
nomes22 = ""