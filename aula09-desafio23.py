#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA
#UM DOS DÍGITOS SEPARADOS.
#EX: DIGITE UM NÚMERO: 1834
#UNIDADE:4
#DEZENA:3
#CENTENA:8
#MILHAR:1

num=int(input("Digite um número: "))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))