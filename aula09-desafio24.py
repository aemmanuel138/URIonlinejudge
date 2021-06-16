#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA COM
#O NOME 'SANTO'.

cidade=str(input("Digite o nome da cidade: ")).strip()
print(cidade[:5].upper()=="SANTO")
