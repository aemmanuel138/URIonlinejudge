x = int(input())
if x % 2 != 0:
    for c in range (x, x+12,2):
        print(c)
else:
    x = x+1
    for c in range (x, x+12,2):
        print(c)
