def lista ():

  lista = eval(input())


  primeiro_valor = lista[0]
  nova_lista =[]

  for valores in lista:
      if valores <= primeiro_valor:
          nova_lista.append(valores)

  return nova_lista


print(*lista())