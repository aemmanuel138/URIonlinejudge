a, b, c, d=map(int,input().split())

#CONVERSÃO DE HORAS EM MINUTOS
h1=(a*60)+b
h2=(c*60)+d
hf=int(0)
mf=int(0)
hora=int(0)
if h2 > h1:
    hf=h2-h1
    hora=hf//60
    mf=hf-(hora*60)
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora, mf))
if h1 > h2:
    hf=1440-(h1-h2)
    hora = hf // 60
    mf = hf-(hora*60)
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora, mf))
if h1 == h2:
    hora=24
    mf=0
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora,mf))
