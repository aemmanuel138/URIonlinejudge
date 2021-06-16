primeiro = int(input("1º TERMO DA P.A.: "))
razao = int(input("RAZÃO DA P.A.: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        termo += razao
        cont += 1
        print("{}".format(termo), end=' → ')
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print('FIM')