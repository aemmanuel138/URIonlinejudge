num=input().split(" ")
a, b, c = num
maior = ((int(a))+(int(b))+abs((int(a))-(int(b))))/2
resultado = ((int(maior)+(int(c)))+abs((int(maior))-(int(c))))/2
print("{:.0f} eh o maior".format(resultado))

