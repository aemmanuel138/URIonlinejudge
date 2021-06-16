primeiro = int(input("1º TERMO DA P.A.: "))
razao = int(input("RAZÃO DA P.A.: "))
termo = primeiro
cont = 1
while cont <= 10:
    termo += razao
    cont += 1
    print("{}".format(termo), end=' → ')
print("FIM!")