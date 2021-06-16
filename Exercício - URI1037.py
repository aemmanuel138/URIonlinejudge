entrada=float(input())
if 0 <= entrada <= 25:
    intervalo='Intervalo [0,25]'
elif 25 < entrada <=50:
    intervalo='Intervalo (25,50]'
elif 50 < entrada <=75:
    intervalo='Intervalo (50,75]'
elif 75 < entrada <= 100:
    intervalo='Intervalo (75,100]'
else:
    intervalo='Fora de intervalo'
print(intervalo)
