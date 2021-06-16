#ESCREVA UM PROGRAMA QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO
#E MOSTRE SEU NOVO SALÁRIO COM 15% DE AUMENTO

sal=float(input("Qual o salário do funcionário? "))
aum=sal+(sal*0.15)
print("O valor do salário reajustado do funcionário é de R$ {:.2f}".format(aum))
