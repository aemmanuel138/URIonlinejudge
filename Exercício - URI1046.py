a, b=map(int,input().split())
inicio=int(0)
final=int(0)
if a > b:
    inicio=a
    final=b
    tmp= 24 - (inicio-final)
elif a == b:
    tmp=24
else:
    inicio=b
    final=a
    tmp=inicio-final
print("O JOGO DUROU {} HORA(S)".format(tmp))
