#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR
#OU ÍMPAR.
num=int(input("Digite um número qualquer: "))
resultado=num%2
if resultado==0:
    print("O número {} é PAR.".format (num))
else:
    print("O número {} é ÍMPAR.".format (num))
