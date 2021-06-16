from time import sleep
print(10*"=","PROGRAMA DE ANALISE DE VALORES",10*"=")
x = int(input("Digite um valor: "))
y = int(input("Digite um valor: "))
opcao = 0
soma = 0
mult = 0
while opcao != 5:
    print('''OPÇÕES:
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIOR DO PROGRAMA''')
    opcao = int(input("DIGITE SUA OPÇÃO: "))
    if opcao == 1:
        soma = x + y
        print("SOMA\n{} + {} = {}".format(x, y, soma))
    elif opcao == 2:
        mult = x * y
        print("MULTIPLICAÇÃO\n{} x {} = {}".format(x, y, mult))
    elif opcao == 3:
        if x > y:
            maior = x
        else:
            maior = y
        print("MAIOR VALOR {}".format(maior))
    elif opcao == 4:
        print("INFORME OS VALORES NOVAMENTE:")
        x = int(input("Digite um valor: "))
        y = int(input("Digite um valor: "))
    elif opcao == 5:
        print("FINALIZANDO...")
        sleep(2)
    else:
        print("Opção inválida. Tente novamente!")
    print('<=>' * 12)
print("PROGRAMA ENCERRADO")
