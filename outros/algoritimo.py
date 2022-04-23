import math

print( )
print('\033[1;33;40m-=-\033[m'*20)
print( )
print('                      \033[4;37;40mCALCULADORA\033[m')
print( )

n1 = float(input('           Digite o primeiro número: '))
op =       input('           Digite a operação:        ')
n2 = float(input('           Digite o segundo número:  '))

if   op == '+' : 
    res = f'           A soma entre {n1} e {n2} é = {n1+n2}'
elif op == '-' :
    res = f'           A subtração entre {n1} e {n2} é = {n1-n2}'
elif op == '*' :
    res = f'           A multiplicaçao entre {n1} e {n2} é = {n1*n2}'
elif op == '/' :
    res = f'           A divisão entre {n1} e {n2} é = {n1/n2}'
elif op == '**':
    res = f'           A potencia da base {n1} pelo expoente {n2} é = {n1**n2}'
elif op == 'rq':
    res = f'           A raiz quadrada de {n1} é = {math.sqrt(n1)}'
elif op == '//':
    res = f'           A divisão inteira entre {n1} e {n2} é = {n1//n2}'
elif op == '%' :
    res = f'           O resto da divisão entre {n1} e {n2} é = {n1%n2}'
else:
    res =  '                \033[1;31;40mFALHA NA OPERAÇÃO\033[m'

print(res)
print( )
print('\033[1;33;40m-=-\033[m'*20)
print( )
