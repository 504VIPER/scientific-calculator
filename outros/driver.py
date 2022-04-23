nome = 'José'
idade = 33
print('O %s tem %d anos.' % (nome, idade)) # Python 2 
print('O {} tem {} anos.'.format(nome, idade)) # Python 3
print(f'O {nome} tem {idade} anos.') # Python 3.6+

print("Olá, Mundo!")

print(74)

print(77+23)

print('7'+'4')

print("Olá Mundo",1)

nome='Patrick'
idade=14
peso=51.9
print(nome,idade,peso)

msg='olá'
print(msg)









print('PERGUNTAS E EXEMPLOS')

nome=input('qual é seu nome?')
idade=input('quantos anos você tem?')
peso=input('quanto você pesa?')
print(nome,idade,peso)

nome=input('qual é seu nome?')
msg='Seja bem vindo(a)'
print(msg,nome)

nome=input('qual é seu nome?')
print('Seja  bem vindo {}!'.format(nome))

pergunta=input('Como você está se sentindo?')
print('Que bom :)')

nome=input('qual é seu nome?')
msg='Seja bem vindo'
jpj='fique a vontade'
print(msg,nome,jpj)









print('DATA')

dia=input('que dia é hoje?')
mês=input('em que mês estamos?')
ano=input('em que ano estamos?')
print(dia,mês,ano)









print('DATA DE NASCIMENTO')

dia=input('Dia ?')
mês=input('Mês ?')
ano=input('Ano ?')
msg=('Você nasceu em')
tt=('correto?')
ui=('de')
print(msg,dia,ui,mês,ui,ano,tt)









print('EXEMPLOS COM IS')

a = input('Digite algo: ')
print('O tipo primitivo desse desse valor é',type(a))
print('Só tem espaços? ',a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanúmerico? ', a.isalnum())
print('Está em maisculo? ', a.isupper())
print('Está em minusculo? ', a.islower())
print('Está capitalizado? ', a.istitle())









print('ORDEM DE PROCEDÊNCIA')

print('1- () ')
print('2- ** ')
print('3- *   /   //   % ')
print('4- +   - ')

print(5+3*2==11)
print(3*5+4**2==31)
print(3*(5+4)**2==243)
print(pow(5,3))









print('EXEMPLOS COM PRINT')

print('Olá'+'Olá')
print('Olá'*20)
print('='*20)
nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {nome:<20}!')
nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {nome:>20}!')
nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {nome:^20}!')
nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {nome:=^20}!')









print('ANTECESSOR E SUCESSOR DE UM NÚMERO')

n1 = int(input('Digite um número: '))
print(f'O antecessor de {n1} é {n1 - 1}')
print(f'O sucessor de {n1} é {n1 + 1}')









print('DOBRO, TRIPLO E A RAIZA QUADRADA DE UM NÚMERO')

n1 = float(input('Digite o primeiro número: '))
print(f'O dobro de {n1} vale {n1*2}')
print(f'O triplo de {n1} vele {n1*3}')
print(f'A raiz quadrada de {n1} vale {n1 ** (1 / 2):.2f}')









print('MÉDIA')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print(f'A média das notas é: {(n1 + n2)/ 2}')









print('MÉTROS EM CM, CM EM ML')

n1 = int(input('Quantos metros? '))
print(f'{n1} metros é igual a {n1*100} centimetros')
print(f'E {n1*100} centimetros é igual a {n1*1000} milimetros')









print('TABUADA')

n1=int(input('Digite um número: '))
print("="*12)
print(f'{n1} x  1 = {n1*1}')
print(f'{n1} x  2 = {n1*2}')
print(f'{n1} x  3 = {n1*3}')
print(f'{n1} x  4 = {n1*4}')
print(f'{n1} x  5 = {n1*5}')
print(f'{n1} x  6 = {n1*6}')
print(f'{n1} x  7 = {n1*7}')
print(f'{n1} x  8 = {n1*8}')
print(f'{n1} x  9 = {n1*9}')
print(f'{n1} x 10 = {n1*10}')
print("="*12)









print('CONVERSOR DE REAL EM DOLLAR (SE DOLLAR = 5,59)')

n1 = float(input('Quantos reais você tem? R$'))
print(f'Com R${n1:.2f} você concegue comprar US${n1//5.59:.2f}')









print('GRAUS CELSIUS EM FAHRENHEIT')

gr = float(input('Qual é a temperatura em °C: '))
print(f'A temperatura de {gr}°C corresponde a {(gr*(9/5))+32:.1f}°F')









print('ARREDONDAMENTO DE UM NÚMERO')

from math import trunc
n1 = float(input('Digite um valor: '))
print(f'O valor digitado foi {n1} e a sua porção inteira é {trunc(n1)}')
#----------------------------------ou----------------------------------
print(f'O valor digitado foi {n1} e a sua porção inteira é {int(n1)}')









print('VALOR DA HIPOTENUSA DE UM TRIANGULO RETÂNGULO')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print(f'O valor da hipotenusa é = {(hip):.2f}')
#-----------------------ou-----------------------
import math
hip2 = math.hypot(co, ca)
print(f'O valor da hipotenusa é = {hip2:.2f} ')









('SENO, COSSENO E TANGENTE')

import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {int(angulo)}º tem o seno de {seno:.2f}')
print(f'O ângulo de {int(angulo)}º tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {int(angulo)}º tem a tangente de {tangente:.2f}')









print('SORTEIO DE UM NOME')

from random import choice
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
print(input(f'O nome escolhido foi: {choice(lista)}'))









print('ORDEM ALEATÓRIA')

from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(lista)









print('MÚSICA')

# from pygame import mixer

# mixer.init()
# mixer.music.load(f'c:\Users\Patrick\.vscode\PASTA\tp.mp3')
# mixer.music.play()









print('MANIPULANDO TEXTO')

frase = "Python Teste"

print(frase[3]) # valor na sua casa 

print(frase[3:5]) # o ultimo valor sempre sera um a menos(ex:3:5 vai ser o 3 e o 4)

print(frase[7:12]) # do 7 ao 11

print(frase[1:12:2]) # do 1 até o 11 pulando de 2 em 2 

print(frase[::2]) # frase inteira pulando de 2 em 2

print(frase[:6]) # do começo até o 6

print(frase[7:]) # do 7 até o final 

print(frase[7::3]) # do 7 até o final pulando de 3 em 3

print(frase[:9:3]) # do começo até o 9 pulando de 3 em 3

print(len(frase)) # quantidade de caracteres dentro da frase

print(frase.count('e')) # quantidade de vezes que o (e) aparece na frase

print(frase.count('y',0,6)) # quantidade de vezes que o (y) aparece na frase do 0 até o 5

print(frase.find('est')) # em que posição o (est) começou, caso não encontre (est) o valor será -1

print('Python' in frase) # mostrará se existe (Python) na frase

print(frase.replace('Python','Android')) # irá trocar de lugar o Python com o Android

print(frase.upper()) # irá colocar todas as letras da frase em maiusculas 

print(frase.lower()) # irá colocar todas as letras da frase em minusculas

print(frase.capitalize()) # irá colocar a primeira letra da frase em maiuscula

print(frase.title()) # irá colocar toda primeira letra de cada palavra da frase em maiuscula

print(frase.strip()) # irá remover todo espaço no começo e no final da frase

print(frase.rstrip()) # irá remover todo espaço no final da frase

print(frase.lstrip()) # irá remover todo espaço no começo da frase

print(frase.split()) # cria uma divisão entre as palavras, reiniciando o valor de cada uma delas
#criando uma lista, e cada palavra agora tem uma ordem crescente dentro dessa lista, sendo 0 a primeira palavra

print('-'.join(frase)) # junta as palavras dividas por (frase.split()) com -
#apenas se o frase.split() não estiver em print e as alterações forem salvas

frase = frase.split()
print('-'.join(frase)) 

print("""Olá
tudo bem ?
ok """) # coloca uma frase ou texto grande tudo junto com """ no começo e no final









print('ANALISDOR DE NOME')

print( )
frase = str(input('Digite seu nome completo? '))
print( )

print('Analisando seu nome...')

print(f'Seu nome em maiúsculo é: {frase.upper()}')

print(f'Seu nome em minúsculo é: {frase.lower()}')

print(f'Seu nome tem ao todo {len(frase) - frase.count(" ")} letras')

print(f'Seu primeiro nome tem {frase.find(" ")} letras')
#----------------------ou---------------------------
sep = frase.split()
print(f'Seu primeiro nome tem {len(sep[0])} letras')
print( )









print('SEPARADOR DE DIGITOS DE NUMEROS')

num = int(input('Digite um número: '))

n = str(num)

print(f'Unidade = {n[3]}')

print(f'Dezena  = {n[2]}')

print(f'Centena = {n[1]}')

print(f'Milhar  = {n[0]}')

#----------------------ou---------------------

print(f'Unidade = {num // 1 % 10}')

print(f'Dezena  = {num // 10 % 10}')

print(f'Centena = {num // 100 % 10}')

print(f'Milhar  = {num // 1000 % 10}')









print('NOME NA CIDADE')

print( )
cid = str(input('Qual é o nome da cidade? ')).strip()
print(f'A cidade de {cid} tem Santo no nome?')
print(cid[:5].upper() == 'SANTO')
print('|True = Verdadeiro')
print('|False = Falso')
print( )









print('NOME NO NOME')

nome = str(input('Qual é seu nome completo? ')).strip()
print('seu nome tem Silva?')
print('SILVA' in nome.upper())
print('|True = Verdadeiro')
print('|False = Falso')









print('CONTAGEM DE UMA LETRA')

frs = str(input('Digite uma frase: ')).upper().strip()
print('Analisando a frase...')

print(f'A letra (a) se repete {frs.count("A")} vezes na frase')

print(f'A primeira letra (a) apareceu na posição {frs.find("A")}')

print(f'A ultima letra (a) apareceu na posição {frs.rfind("A")}')









print('PRIMEIRO E ULTIMO NOME')

nome = str(input('Digite seu nome completo: ')).strip()
x = nome.split()
print(f'{x}')
print('Analisando o nome...')
print(f'Primeiro nome = {x[0]}')
print(f'Ultimo nome = {(x[len(x)-1])}')









print('IF E ELSE')

nome = str(input('Qualé seu nome? '))
if nome == 'Patrick':
    print('Que nome lindo você tem!')
else:
    print('Que nome normal você tem!')
print(f'Bom dia {nome}')









print('JOGO DE ADIVINHAÇÂO')

from random import randint
from time import sleep

print( )
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-' * 20)
print( )

n1 = randint(0 , 5)
n2 = int(input('Digite um número: '))

print('Processando...')
sleep(1)

if n2 == n1:
    print('Parabéns, você acertou')
else:
    print(f'Infelizmente você errou')

print(f'Pensei no número {n1}')
print( )









print('PAR OU IMPAR')

print( )
num = int(input('Me diga um número: '))

if num % 2 == 0:
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é IMPAR')









print('ANO BISSEXTO')

from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto')
else:
    print(f'O ano de {ano} não é Bissexto')









print('MENOR E MAIOR VALOR')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número:  '))
c = int(input('Digite o terceiro número: '))

if a<b and a<c:
    print(f'O menor número é o {a}')
if b<a and b<c:
    print(f'O menor número é o {b}')
if c<a and c<b:
    print(f'O menor número é o {c}')
if a>b and a>c:
    print(f'O maior número é o {a}')
if b>a and b>c:
    print(f'O maior número é o {b}')
if c>a and c>b:
    print(f'O maior número é o {c}')









print('ANALISANDO TRIÂNGULO v1.0')

print( )
print('-=-'*10)
a = int(input('Qual é o primeira segmento? '))
b = int(input('Qual é o segundo segmento? '))
c = int(input('Qual é o terceira segmento? '))
print('-=-'*10)
if a < b + c and b < a + c and c < a + b :
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')
print( )









print('Condições Aninhadas')

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome == 'Ana' or 'Cláudia' or 'Jéssica' or 'Juliana':
    print('Belo nome feminino')
else :
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}')









print('Estrutura de repetição for')

for c in range (0,6): # Oi 6 vezes
    print('Oi')
print('FIM')

for c in range (0,7): # do 1 até o 6
    print(c)
print('FIM')

for c in range (6,0): # nada
    print(c)
print('FIM')

for c in range (6,0,-1): # do 6 até o 1
    print(c)
print('FIM')

for c in range (1,8, 2): # do 1 até 8 de 2 em 2
    print(c)
print('FIM')

n = int(input('Digite um número ')) # do 0 até o número digitado
for c in range (0, n+1):
    print(c)
print('FIM')

i = int(input('Início: ')) # número de início
f = int(input('Fim: ')) # número final
p = int(input('Passo: ')) # pulo (ex: 2 = de 2 em 2)
for c in range (i, f+1, p): # do início até o fim de pulo em pulo
    print(c)
print('FIM')

for c in range(0, 3): # vai repitir o (n) 3 vezes
    n = int(input('Digite um valor: '))
print('FIM')

s = 0
for c in range(0, 3): # vai pedir 3 valores e fazer a soma deles 
    n = int(input('Digite um valor: '))
    s += n
print(f'A soma dos valores digitados é = {s}')









print('Estrutura de repetiçâo While')

c = 1 # do 1 ao 9
while c < 10: # while = enquanto
    print(c)
    c += 1
print('Fim')

n = 1
while n != 0: # vai perguntar um valor a só vai parar quando o valor for 0
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: ')) # vai perguntar um valor
    r = str(input('Quer continuar? [S/N] ')).upper() # se responder S ele continua, se N ele para 
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: ')) # vai perguntar um valor
    if n != 0: # se o valor for 0 ele para de perguntar 
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares') # mostra o número de numeros pares e impares









print('Interrompendo repetições While')

cont = 1
while cont <= 10:
    print(cont, ' -> ', end=' ')
    cont += 1
print('Acabou')

n = 0
cont = 0
while cont < 3: # ou while cont != 3
    n = int(input('Digite um número: ')) # ler 3 números e encerrar o programa
    cont += 1

n = 0
s = 0
while True: # enquanto verdade
    n = int(input('Digite um número: '))
    if n == 999: # se o n == 999
        break # interromper o while e irá executar oq esta fora do while 
    s += n
print(f'A soma vele {s}')









print('Tuplas')
# TUPLAS SÃO IMUTÁVEIS

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(lanche) # irá mostra a tupla lanche

print(lanche[1]) # irá mostra lanche 1, sendo lanche[1] = Suco

print(lanche[-2]) # irá mostra lanche -2, sendo lanche[-2] = Pizza, pois lanche[-3] seria Suco e etc

print(lanche[1:3]) # irá mostra do elemento 1 até o 2, pois ele sempre desconsidera 1 nesse caso

print(lanche[:2]) # irá mostra do ínicio até o elemento 1, pois desconsidera 1 nesse caso

print(lanche[-2]) # irá mostra do elemento -2 até o final

print(len(lanche)) # irá mostrar o quantidade de elementos dentro de lanche

print(sorted(lanche)) # irá mostrar o a tupla em ordem

for comida in lanche: # irá mostrar o print abaixo na corrente lanche
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

for comida in range (0, len(lanche)): # irá mostra a corrente de 0 até o último elemento de lanche
    print(f'Eu vou comer {lanche[comida]}') # irá mostrar o nome da comida que está em cada elemento que deveria ser mostrado
print('Comi pra caramba')

for pos, comida in enumerate(lanche): # irá mostrar a corrente, sendo pos a posição (com o uso do enumerate) e comida o elemento da tupla
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # Tupla a junto a Tupla b
print(c)

print(c.count(5)) # irá mostrar quantas vezes o 5 aparece na tupla c 

print(c.index(5)) # irá mostrar em que posição o 5 aparece pela primeira vez

print(c.index(5, 2)) # irá mostrar em que posição o 5 aparece pela primeira vez a partir do elemento 2

pessoa = ('Gustavo', 39, 'M', 99.88 )
del(pessoa) # irá apagar a tupla pessoa da memória
print(pessoa)

from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10) ) # sortear 5 valores de 1 a 10 dentro de uma tupla

print(f'Os valores sorteados foram: ', end= '')
for c in n: # fazer uma quebra dos parênteses
    print(f'{c} ', end= '')

print(f'\nO maior valor foi {max(n)}') # mostrar o maior valor dento de n 
print(f'O menor valor foi {min(n)}') # mostrar o menor valor dentro de n









print('Listas')
# LISTAS SÃO MUTÁVEIS

num = [2, 5, 9, 1] # lista

num[2] = 3 # irá adicionar o 3 na posição 2

num.append(7) # irá adicionar o 7 no final da lista

num.insert(2, 0) # irá adicionar o 0 na posição 2

num.sort() # irá colocar os valores da lista em ordem

num.sort(reverse= True) # irá colocar os valores da lista em ordem inversa

len(num) # irá mostrar a quantidade de elementos dentro da lista
print(len(num))

num.pop() # irá remover o ultimo valor da lista 
num.pop(2) # irá remover o valor que está na posição 2

num.remove(2) # irá remover o 2 na primeira ocorrência dele

if 4 in num: # irá remover o 4 se o 4 estiver na lista
    num.remove(4)

for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')

valores = [] # começar uma lista vazia assim
valores = list() # ou assim

for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

print(valores)

a = [1, 2, 3, 4]
b = a
b[1] = 5 # irá torcar adicionar o valor 5 na posição 1 na lista a e na lista b, já que há uma ligação entre as duas
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [1, 2, 3, 4]
b = a[:] # irá fazer b receber todos os itens de A, assim não hávera uma ligação entre as duas
b[1] = 5 # e o 5 será adicionado na posição 1 só na lista B e não na posição A
print(f'Lista A: {a}')
print(f'Lista B: {b}')


teste = []
teste.append('Gustavo')
teste.append(40)
print(teste) # lista teste = ['Gustavo', 40]

pessoas = []
pessoas.append(teste[:]) # para copiar a lista teste na lista pessoas
teste[0] = 'Maria' # atualizar o valor da lista teste no elemento 0
teste[1] = 22      # atualizar o valor da lista teste no elemento 1
pessoas.append(teste[:]) # adicionar os elementos atuais da lista teste na lista pessoas
print(pessoas) # lista pessoa = [['Gustavo', 40], ['Maria', 22]], lista dentro de lista


galera = [['João', 19], ['Ana', 33], ['Joaqui', 13], ['Maria', 45]] # listas dentro de uma lista
print(galera) # lista galera = [['João', 19], ['Ana', 33], ['Joaqui', 13], ['Maria', 45]]
print(galera[0]) # irá mostrar a lista 0 na lista galera (['João', 19])
print(galera[0][0]) # irá mostrar o elemento 0 na lista 0 da lista galera (João)
print(galera[2][1]) # irá mostra o elemento 1 na lista 2 da lista galera (13)

for c in galera:
    print(c) # irá mostra em cada linha a lista da lista galera
    print(c[0]) # irá mostrar em cada linha apenas o elemento 0 de cada lista da lista galera
    print(f'{c[0]} tem {c[1]} anos de idade...')
 

pessoas = []
dados = []
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(str(input('Idade: ')))
    pessoas.append(dados[:]) # copiar a lista dados para a lista pessoas
    dados.clear() # irá limpar a lista dados para repitir o proceso masi 2 vezes
print(pessoas)

maior = menor = 0
for c in pessoas:
    if c[1] >= 18: # se o elemento 1 de cada lista da lista pessoas for maior ou igual 18
        print(f'{c[0]} é maior de idade') # elemento 0 é maior de idade
        maior += 1 # adicionar 1 ao contador
    else:
        print(f'{c[0]} é menor de idade') # elemento 0 é menor de idade
        menor += 1 # adicionar 1 ao contador
print(f'Temos {maior} maiores e {menor} menores de idade')









print('Dicionários')
dinionário = {} # criar um dicionário vazio assim
dicionário = dict() # ou assim

pessoas = {'nome': 'Gustavo', 'sexo': 'M','idade': 22}

print(pessoas) # mostrar dicionario pessoas

print(pessoas['nome']) # mostrar elemento nome (Gustavo)

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys()) # irá mostrar os as chaves do dicionario pessoas 
# chaves = 'nome', 'sexo', 'idade'

print(pessoas.values()) # irá mostrar os valores dentro de todas as chaves

print(pessoas.items()) # irá mostar os itens do dicionario dentro de uma tupla, dentro de uma lista
# e cada chave dentro de uma tupla com seu devidos valores

for k in pessoas.keys(): # mostrar uma corrente apenas com as chaves
    print(k)

for v in pessoas.values(): # mostrar uma coarrente apenas com os valores de cada chave em cada linha
    print(v)

for k, v in pessoas.items():  # mostrar a corrente com as chaves e os valores das chaves, sendo 'k' a chave e 'v' os valores
    print(f'{k} = {v}')

del pessoas['sexo'] # irá apagar a chave 'sexo' do dicionario
print(pessoas)

pessoas['nome'] = 'Leandro' # irá substituir o elemento 'Gustavo' dentro da chave 'nome' por 'Leandro')

pessoas['peso'] = 98.5 # irá adicionar uma chave com seu elemento ao final do dicionario


brasil = [] # lista
estado1 = {'uf': 'Rio de Jaeneiro', 'sigla': 'RJ'} # dicionário
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'} # dicionário

brasil.append(estado1) # adicionar o dicionário estado1 na lista brasil
brasil.append(estado2) # adicionar o dicionário estado2 na lista brasil

print(brasil)
print(brasil[0]) # irá mostrar o elemento 0 dentro da lista brasil, que seria o dicionário estado1
print(brasil[0]['uf']) # irá mostrar a chaver 'uf' no elemento 0 da lista)


estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')) # chave 'uf' do dicionário estado será o input dado
    estado['sigla'] = str(input('Sigla do Estado: ')) # chave 'sigla' do dicionário estado será o input dado
    brasil.append(estado.copy()) # adicionar um cópia do dicionario na lista
print(brasil)

for e in brasil: 
    for c, v in e.items(): # mostrar a corrente com as chaves e os valores das chaves, sendo 'c' a chave e 'v' os valores
        print(f'O campo {c} tem valor {v}')

for e in brasil:
    for v in e.values(): # mostrar a corrente com os valores de todas as chaves
        print(v, end=' ')
    print()









print('FUNÇÕES')('DEV')
def lin(): # atribui o valor 'print('-' * 30)' a função 'lin'
    print('-' * 30)

lin() # sempre que usar 'lin' vai ser mostrado o valor atribuido a ela
print('           PYTHON')
lin()


def titulo(txt): # 'txt' vai ser a função com valor atribuida a 'titulo' no programa principal
    lin() # irá mostrar o 'lin' com o 'txt' embaixo na mesma quantidade de valores atribuidos a 'titulo'
    print(txt)
    lin()

#Progrma Principal
titulo('           CURSO EM VIDEO')
titulo('                 Oi')
titulo('               TESTE')


def soma(a, b): # agora terá dois parametros que são os valores atribuidos na 'soma'
    s = a + b
    print(f'A soma entre {a} e {b} é = {s}')

#Programa Principal
soma(2, 5) # pode declarar os valores 'a' e 'b' assim
soma(a = 2, b = 5) # ou assim
soma(a = 5, b = 2) # ou também assim
# soma não pode receber valores maiores ou menores que a quantidade de parametros atribuidas no def


def contador(*num): # '(*num)' será a quantidade de valores dentro do contador que receberá o parametro 'num'
    print(num) # mostrará os valores no 'contador' em forma de tupla
    print(f'Recebi os valores {num} e ao todo são {len(num)} números')
    for v in num: # um for com o 'num', que será mostrado para cada 'contador'
        print(f'{v} ', end='')
    print('Fim')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst): # parâmentro 'lst' é o valor atribuido a dobra, que no caso é uma lista
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2 # dobrar cada valor referente ao parâmetro
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


def soma(*valores):
    s = 0
    for num in valores: # para cada valor em 'valores' irá somar esse valor na variavel 's'
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)


print('FUNÇÕES (parte 2)')

# help(print)
# print(input.__doc__)
# help(input)


def contador(i, f, p): # criar uma documentação para a função contador 
    """ 
    -> Faz uma contagem e mostra na tela.
    :param i: ínicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Patrick
    """
    cont = i
    while cont <= f:
        print(f'{cont} ', end='')
        cont += p
    print('FIM!')


# contador(0, 10, 2)
help(contador) # mostrar a documentação no terminal



def somar(a = 0, b = 0, c = 0): # 'a b c = 0' se o não tiver valor para 'a b c' na função 'somar' / parâmetros opcionais
    s = a + b + c
    print(f'A soma vale {s}')

somar(2)



def teste():
    global d
    d = 7 # 'd' global agora vale 7, por conta do 'global d'
    n = 3 # n local
    x = 8
    print(f'Na função teste n vale {n}') # 'n'seria o 'n' local
    print(f'Na função teste x vale {x}') # 'x' só é aceito no teste pois ele tem um escopo local

d = 5
n = 2 # n global
print(f'No programa principal n vale {n}')
# por isso o 'x' não é aceito no programa principal
teste()



def soma( a = 0, b = 0, c = 0):
    s = a + b + c
    return s

r1 = soma(2, 3, 5)
r2 = soma(3, 4)
r3 = soma(9)

print(f'Os resultados foram {r1}, {r2} e {r3}')



def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

#Programa principal
num = int(input('Digite um valor: '))

print(par(num)) # mostrar o retorno

if par(num): # se retorno for 'True'
    print('É par')
else:
    print('Não é par')









print('Tipos de Erros')
# NameError
# ValueError
# ZeroDivisionError
# TypeError
# IndexError
# KeyError
# EOFError
# Keyboardinterrupt
# OSError
# ConnectionError
# RuntimeError


print('Tratamentos de Erros')
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os dados que você digitou.')

except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')

except KeyboardInterrupt:
    print('\nO usuário preferio não informar os dados!')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre! Muito obrigado!')
