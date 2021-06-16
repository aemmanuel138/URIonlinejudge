salario=float(input())
if salario <= 400:
    perc=int(15)
    reajuste = salario * (perc/100)
    novo=salario+reajuste
elif 400 < salario <= 800:
    perc=int(12)
    reajuste = salario * (perc/100)
    novo = salario + reajuste
elif 800 < salario <= 1200:
    perc=int(10)
    reajuste = salario * (perc/100)
    novo = salario + reajuste
elif 1200 < salario <= 2000:
    perc = int(7)
    reajuste = salario * (perc/100)
    novo = salario + reajuste
else:
    perc = int(4)
    reajuste = salario * (perc/100)
    novo = salario + reajuste

print('Novo salario: {:.2f}'.format(novo))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(perc))
