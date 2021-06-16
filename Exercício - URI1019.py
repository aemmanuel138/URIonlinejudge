n=int(input())
#CALCULO DE QUANTAS HORAS
h=n//3600
n=n-h*3600
#CALCULO DE QUANTOS MINUTOS
m=n//60
n=n-m*60
#SEGUNDOS
s=n
print("{}:{}:{}".format(h,m,s))
