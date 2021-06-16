codigo = int(input("Digite o código do produto: "))

if codigo == 1:
    print("Código 1 : Sul")
elif codigo == 2:
    print("Código 2 : Norte")
elif codigo == 3:
    print("Código 3 : Leste")
elif codigo == 4:
    print("Código 4 : Oeste")
elif codigo == 5 or codigo == 6:
    print("Código : Nordeste")
elif codigo == 7 or codigo == 8 or codigo == 9:
    print("Código : Sudeste")
elif codigo == 10:
    print("Código : Centro-Oeste")
elif codigo == 11:
    print("Código : Noroeste")
else:
    print("Produto Importado")
