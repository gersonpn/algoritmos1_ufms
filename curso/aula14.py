#laço de repetição while
# Enquanto a codição for verdadeira, o bloco de código será executado

condicao = True


while condicao:
    nome = input('Digite seu nome: ')
    if nome != 'sair':
        print(f'Olá {nome}')

    if nome == 'sair':
        break
print ('Fim do programa')
