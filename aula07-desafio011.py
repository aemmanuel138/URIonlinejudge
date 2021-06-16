#ESCREVA UM PROGRAMA QUE LEIA A ALTURA E LARGURA DE UMA PAREDE
#EM METROS, CALCULE A AREA E A QUANTIDADE DE TINTA PARA PINTÁ-LA
#SABENDO QUE UM LITRO PINTA UMA ÁREA DE 2M QUADRADOS
b=float(input("Qual é o comprimento da parede? "))
h=float(input("Qual é a altura da parede? "))
a=b*h
lt=a/2
print("Serão necessários {:.2f} litros de tinta para pintar toda essa parede".format(lt))
