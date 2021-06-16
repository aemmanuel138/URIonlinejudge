num=0
cont=0
for c in range(1,6):
    num = int(input())
    if num % 2 == 0:
       cont += 1
print("{} valores pares".format(cont))
