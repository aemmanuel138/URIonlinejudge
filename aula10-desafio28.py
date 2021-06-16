#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR 'PENSAR' EM UM NÚMERO INTEIRO ENTRE
#0 E 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMEOR ESCOLHIDO
#PELO COMPUTADOR.
#O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU

from random import randint
from time import sleep
pc = randint(0,5) #ESCOLHA ALEATÓRIA DO NÚMERO
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 19)
jogador=int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(4)
if jogador == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(pc,jogador))
