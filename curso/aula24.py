#função enumerate

lista = ['João', 'José', 'Maria']

lista_enumerada = list(enumerate(lista))


#for item in lista_enumerada:
  #  print(item)

  #empacotamento

#for item in lista_enumerada:
 #   indice, nome = item  #empacotamento
 #   print(indice, nome)


for indice, nome in enumerate(lista):
    print(indice, nome)

