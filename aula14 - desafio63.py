n = int(input("Quantos termos? "))
t1 = 0
t2 = 1
print
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1