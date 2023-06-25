contador = 0

while contador < 20:
    contador += 1  # contador = contador + 1 # contador++

    if contador == 6:        # se o contador for igual a 6 ele não exibirá o 6
        print('Vai parar')
        continue


    if contador == 9:      # se o contador for igual a 9 ele para o programa
        print('Vai parar')
        break

    print(contador)


print('Fim do programa')