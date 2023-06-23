a = int (input())
b = int (input())
c = int (input())




if a == 0:
    print('não é uma equação do segundo grau')
else:
    delta = (b ** 2) -4 * a * c
    if delta < 0:
        print ("não possui raízes reais")
    elif delta == 0:
        raiz = - b / ( 2 * a)
        print(raiz)
    else:
        aux = delta  ** 0.5
        raiz1 = (- b + aux) / (2 * a)
        raiz2 = (- b - aux) / (2 * a)
        print (raiz1)
        print (raiz2)

