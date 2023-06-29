def listas():
    lista_a = eval(input("Digite a primeira lista: "))
    lista_b = eval(input("Digite a segunda lista: "))

    unir_listas = lista_a + lista_b
    unir_listas_ordenadas = sorted(unir_listas)

    return unir_listas_ordenadas

print(listas())