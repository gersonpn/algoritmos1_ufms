nome = input('Digite seu nome completo: ')

tamanho = len(nome)


if tamanho <= 4:
    print('Seu nome é curto')
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')