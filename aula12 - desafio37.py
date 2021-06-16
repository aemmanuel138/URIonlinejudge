'''ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O
USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO
[1] PARA BINÁRIO    [2] PARA OCTAL      [3] PARA HEXADECIMAL
'''
from time import sleep
num = int(input("Digite um número inteiro: "))
print(''' Escolha uma das bases para conversão: 
[ 1 ] CONVERTER PARA BINÁRIO
[ 2 ] CONVERTER PARA OCTAL
[ 3 ] CONVERTER PARA HEXADECIMAL''')
opção = int(input("Sua opção: "))
print('PROCESSANDO...')
sleep(2)
if opção == 1:
    print("{} convertido para BINÁRIO é igual a {}".format (num, bin(num)[2:]))
elif opção == 2:
    print("{} convertido para OCTAL é igual a {}".format (num, oct(num)[2:]))
elif opção == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format (num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente.")
