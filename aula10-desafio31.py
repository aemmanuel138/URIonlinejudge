#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
#CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS ATÉ 200KM
#E 0,45 PARA VIAGENS MAIS LONGAS.

dist=int(input("Quantos quilômetros tem o percurso da sua viagem? "))
if dist<=200:
    print("O valor da sua passagem é R$ {:.2f}".format (dist*0.5))
else:
    print("O valor da sua passagem é R$ {:.2f}".format (dist*0.45))
