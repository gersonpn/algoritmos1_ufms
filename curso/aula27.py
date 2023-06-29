#split
#strip() corta espaço

frase = 'olha só que, coisa interessante'

lista_frase_1 = frase.split(",") # separa pela virgula, caso não tenha nada, separa a cada espaço


lista_frase = []

for indice, frase in enumerate(lista_frase_1):
    lista_frase.append(lista_frase_1[indice].strip())





frases_unidas = '-'.join (lista_frase)

print(frases_unidas)