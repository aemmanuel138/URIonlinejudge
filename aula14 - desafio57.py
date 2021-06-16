sexo = str (input("INFORME O SEXO: [M/F] ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("DADO INVÁLIDO! INFORME NOVAMENTE: [M/F] ")).strip().upper()[0]
print("SEXO {} REGISTRADO.".format(sexo))