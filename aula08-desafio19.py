#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
#FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME
#DO ESCOLHIDO.
import random
a1=str(input("Digite o nome do primeiro aluno: "))
a2=str(input("Digite o nome do segundo aluno: "))
a3=str(input("Digite o nome do terceiro aluno: "))
a4=str(input("Digite o nome do quarto aluno: "))
lista=[a1,a2,a3,a4]
rand=random.choice(lista)
print("O(A) aluno(a) escolhido(a) foi {} ".format(rand))



