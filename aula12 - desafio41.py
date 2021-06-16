from datetime import date
nasc=int(input("Qual o ano de nascimento do atleta? "))
atual= date.today().year
idade=atual-nasc
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <=19:
    print("JUNIOR")
elif idade <= 25:
    print("SÊNIOR")
else:
    print("MASTER")
