#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
#O NOME COM TODAS AS LETRAS MAIÚSCULAS
#O NOME COM TODAS AS LETRAS MINÚSCULAS
#QUANTAS LETRAS AO TODO SEM CONSIDERAR ESPAÇOS.
#QUANTAS LETRAS TEM O PRIMEIRO NOME.

nome=str(input('Digite seu nome completo: ')).strip()
print("Seu nome em maiúsculas é {}".format (nome.upper()))
print("Seu nome em minúsculas é {}".format (nome.lower()))
print("Seu nome tem ao todo {} letras".format (len(nome)-nome.count(' ')))
primeiro=nome.split()
print("Seu primeiro nome é {} e ele tem {} letras.".format (primeiro[0], len(primeiro[0])))
