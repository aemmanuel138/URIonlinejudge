while True:
    entrada = int(input())
    anteriorLista = 1  #calcular o próximo elemento da lista
    matriz = []
    lista = [1]  # primeira lista (sempre vai iniciar com 1)
    currentLista = []  # Esta lista servirá para preencher as outras
    if entrada == 0:
        break

    else:

        for e in range(2, entrada + 1):  ## 2 até entrada + 1 ( EX: 2 à 4(3+1))
            lista.append(anteriorLista * 2)  ## EX do primeiro loop: lista = [1,2]
            anteriorLista *= 2  ## nosso anterior passa a valer 2...

        matriz.append(lista)  # Adiciona a primeira lista à matriz
        currentLista = lista  # Nossa lista para os próximos cálculos será a lista inicial

        while (entrada > 1):  # Agora preenchemos as próx listas o Nº de interações é entrada-1
            lista2 = []  # Esta será a nova lista usada
            for e in currentLista:  ## Percorro a lista corrente
                lista2.append(e * 2)  ## Elementos da nova lista serão o dobro da lista corrente

            print()
