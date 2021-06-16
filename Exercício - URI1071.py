x = int(input())
y = int(input())
num = 0
if x < y:
    for c in range (x+1, y):
        if c % 2 != 0:
            num += c
else:
    for c in range (y+1, x):
        if c % 2 != 0:
            num += c
print(num)
