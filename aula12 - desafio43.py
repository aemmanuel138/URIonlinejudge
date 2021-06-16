peso=float(input("Digite o peso: (kg) "))
altura=float(input("Digite a altura: (m) "))
imc=peso/(altura**2)
print("Seu IMC é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO do peso ideal.")
elif imc <= 25:
    print("Vocês está no PESO IDEAL. Parabéns!")
elif imc <= 30:
    print("Você está em SOBREPESO.")
elif imc <= 40:
    print("Você está na faixa de OBESIDADE.")
else:
    print ("Você está na faixa de OBESIDADE MÓRBIDA. Cuidado!")
