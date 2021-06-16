#ESCREVA UM PROGRAMA QUE LEIA O PREÇO DE UM PRODUTO
#E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO
produto=float(input("Qual o valor real do produto? "))
desc=produto-(produto*0.05)
print("O valor deste produto com 5% de desconto ficará por R$ {:.2f}".format(desc))
