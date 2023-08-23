lista = [49, 21, 76, 32, 85, 6, 92, 49, 59, 28]


primeiro_valor = lista[0]

valores_menores = []
valores_maiores = []

for valor in lista[1:]:  # Começamos a partir do segundo elemento (índice 1)
    if valor < primeiro_valor:
        valores_menores.append(valor)
    elif valor > primeiro_valor:
        valores_maiores.append(valor)

lista = sorted(valores_menores) + [primeiro_valor] + (valores_maiores)
print(lista)