#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#QUANTAS VEZES APARECE A LETRA "A".
#EM QUE POSIÇÃO ELE APARECE A PRIMEIRA VEZ.
#EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ.

frase=str(input("Digite uma frase: ")).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))


