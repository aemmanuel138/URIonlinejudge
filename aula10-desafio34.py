#ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O
#VALOR DO SEU AUMENTO.
#PARA SALÁRIOS SUPERIORES A R$ 1.250,00 CALCULE UM AUMENTO DE 10%
#PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%

sal=float(input("Digite o valor do seu salário: "))
if sal > 1250.00:
    print("O seu novo salário será de R$ {:.2f}".format(sal+(sal*0.1)))
else:
    print("O seu novo salário será de R$ {:.2f}".format(sal+(sal*0.15)))
