a=float(input("Digite o valor da primeira reta: "))
b=float(input("Digite o valor da segunda reta: "))
c=float(input("Digite o valor da terceira reta: "))
maior = ((a+b)+abs(a-b))/2
resultado = ((maior+c)+abs(maior-c))/2
cond=(a+b+c)-resultado
if cond > resultado:
    print("As medidas {}, {} e {} formam um triângulo".format(a,b,c))
else:
    print("As medidas {}, {} e {} não formam um triângulo".format(a,b,c))