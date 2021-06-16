#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
#SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
#A MULTA VAI CUSTAR R$ 7,00 POR CADA KM ACIMA DO LIMITE

vel=int(input("Digite a velocidade do veículo: "))
lim=vel-80
if vel > 80:
    print('Sua velocidade é de {}Km/h. Você foi multado em R$ {:.2f}'.format(vel, lim*7))
else:
    print('Sua velocidade é de {}Km/h. Tenha uma boa viagem!'.format(vel))