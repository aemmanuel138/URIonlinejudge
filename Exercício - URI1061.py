cont = 0
soma = 0
media = 0
for c in range(1,7):
    n=float(input())
    if n > 0:
        cont += 1
        soma += n
        media = soma/cont
print ("{} valores positivos".format(cont))
print ("{:.1f}".format (media))
