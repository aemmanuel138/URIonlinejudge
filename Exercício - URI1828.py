entrada = int(input())
cont = 1

for c in range(entrada):
    sheld, raj = map(str,input().split())
    w = 1

    if a == 'tesoura' and b == 'papel':
        w = a
    if a == 'papel' and b == 'pedra':
        w = a
    if a == 'pedra' and b == 'lagarto':
        w = a
    if a == 'lagarto' and b == 'Spock':
        w = a
    if a == 'Spock' and b == 'tesoura':
        w = a
    if a == 'tesoura' and b == 'lagarto':
        w = a
    if a == 'lagarto' and b == 'papel':
        w = a
    if a == 'papel' and b == 'Spock':
        w = a
    if a == 'Spock' and b == 'pedra':
        w = a
    if a == 'pedra' and b == 'tesoura':
        w = a
    if w == a:
        if play == 'she':
            print('Caso #{}: Bazinga!'.format(cont))
        if play == 'raj':
            print('Caso #{}: Raj trapaceou!'.format(cont))