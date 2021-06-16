#ALUGUEL DE CARROS
#ESCREVA UM PROGRAMA UUE PERGUNTE A QUANTIDADE KM PERCORRIDOS POR UM CARRO
#ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO
#A PAGAR, SABENDO QUE O CARRO CUSTA R$60.00 POR DIA E R$0.15 POR KM RODADO

dias=int(input("Quantos dias alugados? "))
km=float(input("Quantos Km rodados? "))
total=(dias*60)+(km*0.15)
print("O total a pagar é de R${:.2f}".format(total))
