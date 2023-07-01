lista = eval(input())

primeiro_item = lista[0]

nova_lista = []

lista_menor = []

lista_maior = []

lista_igual = []



for valor in lista:
    if valor <= primeiro_item:
        lista_menor.append(valor)
    elif valor > primeiro_item:
         lista_maior.append(valor)

lista_igual.append(primeiro_item)
nova_lista = lista_menor + lista_igual + lista_maior
nova_lista.remove(primeiro_item)
print(nova_lista)