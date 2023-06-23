#calculadora com while





while True:
    sair = input('Deseja sair? [s]im ou [n]ão: ').lower().startswith('s')

    if sair == 's' or sair is True:
        print("fim do programa")
        break

    elif sair == 'n':
        n1 = int(input('Digite um número: '))
        n2 = int (input('Digite outro número: '))
        operacao = input('Digite uma operação: +, - , * ou /: ')
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
        else:
            print('Operação inválida')
    else:
        print ('Deseja continuar? [s]im ou [n]ão:')
        if sair == 's':
            continue
        elif sair == 'n':
            print("fim do programa")
            break
