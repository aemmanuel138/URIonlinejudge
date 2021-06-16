soma=0
for num in range(1,7):
    num=int(input("Digite o {}º valor: ".format(num)))
    if num % 2 ==0:
        soma += num
print("A soma dos números pares digitado é igual a {}:".format (soma))
