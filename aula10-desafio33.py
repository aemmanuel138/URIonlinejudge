#FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O
#MENOR.
a=(int(input("Digite o primeiro valor: ")))
b=(int(input("Digite o segundo valor: ")))
c=(int(input("Digite o terceiro valor: ")))
# QUEM É O MAIOR
if a > b and a > c:
    maior=a
if b > a and b > c:
    maior=b
if c > a and c > b:
    maior=c
#QUEM É O MENOR
if a < b and a < c:
    menor=a
if b < c and b < a:
    menor=b
if c < a and c < b:
    menor=c
print("O maior valor digitado foi {}".format(maior))
print("O menor valor digitado foi {}".format(menor))
