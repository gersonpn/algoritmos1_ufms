
#dados mutaveis lista

lista_a = [1, 'nome', True, 23]

lista_b = lista_a.copy()

lista_a[0] = "n2"

print(lista_a)
print(lista_b) # quando o copy é utilizado, ele copia a lista sem alterações, ou seja, mesmo se passar outro valor ele não mudará