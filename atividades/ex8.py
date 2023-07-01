def min_v():

  lista = eval(input())


  min_valor = lista[0]


  for item in lista:
      if item < min_valor:
          min_valor = item

  return min_valor


print(min_v())