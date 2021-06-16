p1=int(input("Digite o primeiro termo da Progressão Aritimética: "))
r=int(input("Digite a razão da Progressão Aritimética: "))
décimo = p1 + (10-1) * r
for c in range(p1,décimo,r):
    print("{}".format(c), end=' → ')
print("FIM!")