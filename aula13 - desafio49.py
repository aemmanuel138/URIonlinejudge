print(''' ESCOLHA UMA DAS OPERAÇÕES:
 [0] SOMA
 [1] SUBTRAÇÃO
 [2] MULTIPLICAÇÃO
 [3] DIVISÃO''')
opção = int(input("A operação desejada é: "))
num = int(input('Digite um número para ver sua tabuada: '))
if opção == 0:
    print('============ A TABUADA DE SOMA DO NÚMERO {} É:============'.format(num))
    for c in range(1, 10 + 1):
        soma = c + num
        print('{} + {:2} = {} '.format(num, c, soma))
elif opção == 1:
    print('============ A TABUADA DE SUBTRAÇÃO DO NÚMERO {} É:============'.format(num))
    for c in range(1, 10 + 1):
        sub = num - c
        print('{} - {:2} = {} '.format(num, c, sub))

elif opção == 2:
    print('============ A TABUADA DE MULTIPLICAÇÃO DO NÚMERO {} É:============'.format(num))
    for c in range(1, 10 + 1):
        mult = c * num
        print('{} x {:2} = {} '.format(num, c, mult))

elif opção == 3:
    print('============ A TABUADA DE DIVISÃO DO NÚMERO {} É:============'.format(num))
    for c in range(1, 10 + 1):
        div = num / c
        print('{} / {:2} = {:.1f} '.format(num, c, div))
else:
    print("OPÇÃO INVÁLIDA!!! TENTE NOVAMENTE.")
