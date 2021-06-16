a=float(input("Digite o primeiro valor: "))
b=float(input("Digite o segundo valor: "))
c=float(input("Digite o terceiro valor: "))
if a < b + c and b < a + c and c < a + b:
    print('O triângulo formado é ', end='')
    if a == b == c:
        print("EQUILÁTERO!")
    elif a != b != c != a:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print('Não forma um triângulo!')
