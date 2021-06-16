#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO
#ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA
#HIPOTENUSA

from math import hypot
catopo=float(input("Digite o valor do cateto oposto: "))
catadj=float(input("Digite o valor do cateto adjacente: "))
hipot=hypot(catopo,catadj)
print("O valor da hipotenusa é {:.2f}".format(hipot))
