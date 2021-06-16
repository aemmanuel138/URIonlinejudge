'''ENTRADA: VALOR DA CASA; SALÁRIO; TEMPO (EM ANOS) PARA PAGAR
PROCESSAMENTO: VALOR DA PRESTAÇÃO MENSAL <= 30% DO SALÁRIO
SAÍDA: EMPRESTIMO APROVADO: VALOR DA PRESTAÇÃO E QUANTIDADE DE PARCELAS
EMPRESTIMO NEGADO: VALOR SUPERIOR A 30% DO SALÁRIO
'''

casa=float(input("Valor da casa: R$ "))
salario=float(input("Salário do comprador: R$ "))
anos=float(input("Quantidade de anos que o empréstimo será quitado: "))

prest=(casa/(anos*12))
perc=salario*0.3
if prest <= perc:
    print("EMPRESTIMO APROVADO: O VALOR DA PRESTAÇÃO É {:.2f} EM {:.0f} PARCELAS".format (prest, (anos*12)))
elif prest > perc:
    print("EMPRESTIMO NEGADO: A PARCELA DE R$ {:.2f} É SUPERIOR A 30% DO SEU SALÁRIO".format(prest))
else:
    print("O VALOR DIGITADO É INVÁLIDO!")
