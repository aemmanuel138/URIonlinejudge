#ESCREVA UM PROGRAMA QUE DEVERÁ SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS
#DE QUATRO ALUNOS DE UMA CLASSE. O PROGRAMA DEVERÁ LER O NOME DOS ALUNOS E
#MOSTRAR A ORDEM SORTEADA.

import random

a1=str(input("Digite o nome do primeiro aluno: "))
a2=str(input("Digite o nome do segundo aluno: "))
a3=str(input("Digite o nome do terceiro aluno: "))
a4=str(input("Digite o nome do quarto aluno: "))
lista=[a1,a2,a3,a4]
random.shuffle(lista)
print("A ordem do sorteio seguirá a sequência{}".format(lista))
