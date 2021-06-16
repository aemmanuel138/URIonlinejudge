n=int(input())
#QUANTOS ANOS
a=n//365
n=n-a*365
#CALCULO DE MESES
m=n//30
n=n-m*30
#DIAS
d=n
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(a,m,d))
