#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.
from datetime import date
ano=int(input("Digite o ano: "))
if ano == 0:
    ano = date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("O ano {} É BISSEXTO".format(ano))
else:
    print("O ano {} NÃO É BISSEXTO".format(ano))