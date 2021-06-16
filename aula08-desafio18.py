#FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA
#O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO
from math import sin, cos, tan, radians
angulo=float(input("Digite a medida do ângulo: "))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print("O angulo {}° retorna os valores: {:.2f} para seno {:.2f} cosseno e {:.2f} tangente".format (angulo, seno,coss,tang))
