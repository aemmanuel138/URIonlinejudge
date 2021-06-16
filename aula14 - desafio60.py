'''from math import factorial
n = int(input("Digite um valor: "))
f = factorial(n)
print("O fatorial de {} é {}.".format(n,f))'''
n = int(input("Digite um valor: "))
c = n
f = 1
while c > 0:
    print("{}".format(c), end='')
    print(" x " if c > 1 else " = ", end="")
    f = f * c
    c -= 1
print("{}".format(f))
