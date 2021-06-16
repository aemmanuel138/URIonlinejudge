#CRIE UM PROGRAMA QUE LEIA QUALQUER NÚMERO PELO TECLADO E MOSTRE NA TELA A
#SUA PORÇÃO INTEIRA. EX: DIGITE UM NÚMERO:6.127 O NÚMERO 6.127 TEM A PARTE
#INTEIRA 6.
from math import trunc
num=float(input("Digite um número: "))
print("O número {} tem a parte inteira {}.".format(num,trunc(num)))