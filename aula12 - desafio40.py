'''ENTRADA: LER DUAS NOTAS
PROCESSO: MEDIA DAS DUAS NOTAS
SAIDA: MEDIA < 5: REPROVADO; MEDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO; MEDIA >= 7.0 APROVADO '''
n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
m = (n1+n2)/2
if m < 5.0:
    print("REPROVADO")
if m > 5.0 and m < 7.0:
    print("RECUPERAÇÃO")
if m >= 7.0:
    print("APROVADO")
