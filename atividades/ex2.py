lista = eval(input("Escreva um numero:"))
print(lista)

primeiro_elemento = lista[0]


for numero in lista:
    if numero <= primeiro_elemento:
        print(numero, end=' ')