num = 0
par = 0
impar = 0
positivo = 0
negativo = 0
for c in range (1, 6):
    num = int(input())
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num > 0:
        positivo += 1
    if num < 0:
        negativo += 1
print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(positivo))
print("{} valor(es) negativo(s)".format(negativo))
