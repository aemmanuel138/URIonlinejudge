a, b, c = map(float, input().split())
m1=float(0)
m2=float(0)
m3=float(0)
if a >= b and a >= c:
    m1=a
    if b>=c:
        n2=b
        n3=c
    else:
        n2=c
        n1=b
if b >= a and b >=c:
    m1=b
    if a>=c:
        m2=a
        m3=c
    else:
        m2=c
        m3=a
if c>= a and c>=b:
    m1=c
    if a>=b:
        m2=a
        m3=b
    else:
        m2=b
        m3=a
if a == b == c:
    m1=a
    m2=b
    m3=c
a=m1
b=m2
c=m3
if a >=(b+c):
    print("NÃO FORMA TRIANGULO")
else:
    if (a**2)==(b**2)+(c**2):
        print("TRIANGULO RETANGULO")
    if (a**2)>(b**2+c**2):
        print("TRIANGULO OBTUSANGULO")
    if (a**2)<(b**2+c**2):
        print("TRIANGULO ACUTANGULO")
    if a==b==c==a:
        print("TRIANGULO EQUILATERO")
    if a==b!=c or a==c!=b or c==b!=a:
        print("TRIANGULO ISOSCELES")
