    while True:
    try:
        opcoes = input().split(" ")
        a, b, c = opcoes

        if int(a) == int(b) == int(c):
            print("*")
        elif int(c) == int(a) != int(b):
            print("B")
        elif int(c) != int(b) == int(a):
            print("C")
        else:
            print("A")
    except EOFError:
        break
