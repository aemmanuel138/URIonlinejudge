#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO
#EM SEGUIDA O PRIMEIRO E O ÚLTIMO SEPARADAMENTE.
#EX: ANA MARIA DE SOUZA
#primeiro=Ana
#último=Souza

n=str(input("Digite seu nome completo: ")).strip()
nome=n.split()
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format (nome[0]))
print("Seu último nome é {}".format (nome[len(nome)-1]))
