a=str(input())
b=str(input())
c=str(input())
if a=='vertebrado':
    if b=='ave':
        if c=='carnivoro':
            animal='aguia'
        else:
            animal='pomba'
    else:
        if c=='onivoro':
            animal='homem'
        else:
            animal='vaca'
else:
    if b=='inseto':
        if c=='hematofago':
            animal='pulga'
        else:
            animal='lagarta'
    else:
        if c=='hematofago':
            animal='sanguessuga'
        else:
            animal='minhoca'
print(animal)