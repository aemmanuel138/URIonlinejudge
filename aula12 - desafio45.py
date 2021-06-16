from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador=randint(0,2)
'''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA'''
jogador=int(input("Qual é a sua jogada? "))
print('<=>'*11)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print('<=>'*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('<=>'*11)
if computador==0:#PEDRA
    if jogador==0:
        print("EMPATE")
    elif jogador==1:
        print("JOGADOR VENCE")
    elif jogador==2:
        print("COMPUTADOR VENCE")
    else:
        print("Jogada inválida")

elif computador==1:#PAPEL
    if jogador==0:
        print("O COMPUTADOR VENCEU!")
    elif jogador==1:
        print("EMPATE!")
    elif jogador==2:
        print("O JOGADOR VENCEU!")
    else:
        print("Jogada inválida")

elif computador==2:#TESOURA
    if jogador==0:
        print("O JOGADOR VENCEU!")
    elif jogador==1:
        print("O COMPUTADOR VENCEU!")
    elif jogador==2:
        print("EMPATE!")
    else:
        print("Jogada inválida")
