from random import randint
comp = randint(0,10)
print("Olá! Escolhi um número entre 0 e 10. Tente acertar!")
acertou = False
cont = 0
while not acertou:
    ent = int(input("Escolha um número: "))
    cont += 1
    if ent == comp:
        acertou = True
        if cont < 3:
            print("Parabéns, você acertou!")
        elif cont < 6:
            print("Você acertou! Mas não teve tanta sorte!")
        else:
            print("Caramba! Quase não acerta!")
print ("O computador escolheu a opção {} e você precisou de {} tentativa(s) para acertar.".format (comp, cont))
