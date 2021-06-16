print('{:=^40}'.format(' VAMO ENTRANO '))
vlr=float(input("Preço das compras: "))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção=int(input("Qual é a opção? "))
if opção==1:
    total=vlr-(vlr*0.1)
    print("Sua compra no valor de R$ {:.2f} terá um desconto de 10%.\n O valor total a pagar será R$ {:.2f}".format (vlr, total))
if opção==2:
    total=vlr-(vlr*0.05)
    print("Sua compra no valor de R$ {:.2f} terá um desconto de 5%.\n O valor total a pagar será R$ {:.2f}".format(vlr, total))
if opção==3:
    parc=vlr/2
    print("Sua compra no valor de R$ {:.2f} será parcelada no cartão em 2X de R$ {:.2f}".format(vlr,parc))
if opção  == 4:
    qtd=int(input("Quantas parcelas? "))
    parc=vlr/qtd
    total=(parc*0.2)+parc
    print("Sua compra no valor de R$ {:.2f} será parcelada no cartão em {}X de R$ {:.2f}".format(vlr,qtd, total))
