a, b, c = map (int, input().split())
#MENOR
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#MEDIO
if a < b and a > c or a < c and a > b:
    medio = a
if b < a and b > c or b < c and b > a:
    medio = b
if c < a and c > b or c < b and c > a:
    medio = c

#MAIOR
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c

print("{}\n{}\n{}\n\n{}\n{}\n{}".format (menor, medio, maior, a, b, c))
