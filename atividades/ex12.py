lista_a = eval(input())
lista_b = eval(input())
lista_c = lista_a + lista_b
lista_crescente = []


while lista_c:
    min_valor = lista_c[0]
    for valor in lista_c:
        if valor < min_valor:
            min_valor = valor

    lista_c.remove(min_valor)
    lista_crescente.append(min_valor)

print(*lista_crescente)