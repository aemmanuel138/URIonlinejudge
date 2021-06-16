
valores=input().split(" ")
a, b, c = valores
pi=3.14159
triangulo=(float(a)*float(c))/2
circulo=((float(c)**2)*pi)
trapezio=((float(a)+float(b))*float(c))/2
quadrado=(float(b)**2)
retangulo=(float(a)*float(b))
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(triangulo,circulo,trapezio,quadrado,retangulo))
