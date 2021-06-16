'''COM BASE NA TABELA ABAIXO, ESCREVA UM PROGRAMA QUE LEIA O CÓDIGO DE UM
ITEM E A QUANTIDADE DESTE ITEM. A SEGUIR, CALCULE E MOSTRE O VALOR DA
 CONTA A PAGAR.
 COD    PRODUTO             PREÇO
 1      CACHORRO QUENTE     R$ 4.00
 2      X-SALADA            R$ 4.50
 3      X-BACON             R$ 5.00
 4      TORRADA SIMPLES     R$ 2.00
 5      REFRIGERANTE        R$ 1.50
ENTRADA
O ARQUIVO DE ENTRADA CONTÉM DOIS VALORES INTEIROS CORRESPONDENTES AO CÓDIGO
E À QUANTIDADE DE UM ITEM CONFORME TABELA ACIMA.
SAÍDA
O ARQUIVO DE SAÍDA DEVE CONTER A MENSAGEM "TOTAL: R$ " SEGUIDO PELO VALOR
A SER PAGO, COM 2 CASAS APÓS O PONTO DECIMAL.

EXEMPLO DE ENTRADA	    EXEMPLO DE SAÍDA
3 2	                TOTAL: R$ 10.00
4 3	                TOTAL: R$ 6.00
2 3	                TOTAL: R$ 13.50

 '''
a, b=input().split()
if (a=='1'):
    print("Total: R$ {:.2f}".format(4.00*float(b)))
if (a=='2'):
    print("Total: R$ {:.2f}".format(4.50*float(b)))
if (a=='3'):
    print("Total: R$ {:.2f}".format(5.00*float(b)))
if (a=='4'):
    print("Total: R$ {:.2f}".format(2.00*float(b)))
if (a=='5'):
    print("Total: R$ {:.2f}".format(1.50*float(b)))
