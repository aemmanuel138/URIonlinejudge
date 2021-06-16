from datetime import date
atual = date.today().year
ano=(int(input("Digite o ano em que você nasceu: ")))
idade=atual-ano
if idade > 18:
    alist=idade-18
    print("Você deveria ter se alistado há {} anos!".format(alist))
elif idade < 18:
    alist=18-idade
    print("Você deverá se alistar em {} anos!". format(alist))
else:
    print("Esta na hora de se alistar!")
