x, y = map (float,input().split())

if x > 0.0:
    if y > 0.0:
        print("Q1")
    if y < 0.0:
        print("Q4")

if x < 0.0:
    if y > 0.0:
        print("Q2")
    if y < 0.0:
        print("Q3")
if x==y==0.0:
        print("Origem")
if x==0 and y!=x:
        print("Eixo Y")
else:
    (print("Eixo X"))
