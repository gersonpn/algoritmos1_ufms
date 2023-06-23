while True:

    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operacao = input('Digite uma operação: +, - , *  / ')

    numero_valido = None #variavel para validar o numero digitado




          #tratamento de erro
    try:
        n1 = float(n1)
        n2 = float(n2)
        numero_valido = True #se o numero for valido, ele recebe True

    except:#se o numero não for valido, ele recebe False
        numero_valido = None #se o numero for invalido, ele recebe None

    if numero_valido is None:#se o numero for invalido, ele exibe a mensagem e continua o programa
        print('Você digitou um número inválido')
        continue#continua o programa

    if operacao not in "+-*/":
        print('Operação inválida') #se a operação for invalida, ele exibe a mensagem e continua o programa
        continue

    if len(operacao) > 1:
       print('Digite apenas uma operação')
       continue




    if operacao == '+':
        resultado = n1 + n2
        print(f'{n1} + {n2} = {resultado}')
    elif operacao == '-':
        resultado = n1 - n2
        print(f'{n1} - {n2} = {resultado}')
    elif operacao == '*':
      resultado = n1 * n2
      print(f'{n1} * {n2} = {resultado}')
    elif operacao == '/':
      resultado = n1 / n2
      print(f'{n1} / {n2} = {resultado}')


    sair = input('Deseja sair? [s]im ou [n]ão: ').lower()#pergunta se deseja sair do programa
    if sair == 'n':
        continue
    elif sair == 's':
      print("fim do programa")
      break