num=(input()).split()
a, b, c = num
a=float(a)
b=float(b)
c=float(c)
if a == 0 or ((b**2)-(4*a*c)) < 0:
    print("Impossivel calcular")
else:
    r1=((-b)+(((b**2)-(4*a*c))**0.5))/(2*a)
    r2=((-b)-(((b**2)-(4*a*c))**0.5))/(2*a)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(r1,r2))
