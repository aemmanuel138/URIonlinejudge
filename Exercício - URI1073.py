n = int(input())
for c in range (1, n+1):
    if c % 2 == 0:
        num = c**2
        print("{}^{} = {}".format (c,2,num))
