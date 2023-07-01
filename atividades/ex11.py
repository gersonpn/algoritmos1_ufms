lista = eval(input())

lista_a = sorted(lista)

print(lista_a)

menor_valor = []

new_lista = []


for valor in lista_a:
    menor_valor = valor

    new_lista.append(menor_valor)

print(*new_lista)