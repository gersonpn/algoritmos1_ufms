try:
    # Abre o arquivo "pessoas.csv" no modo de leitura.
    # Aqui, você está atribuindo o nome do arquivo à variável 'arquivo', mas precisa usar 'open()' para abrir o arquivo.
    arquivo = open('pessoas.csv', 'r')

    # Loop que percorre cada caractere do nome do arquivo (não dos dados do arquivo).
    for registro in arquivo:
        # Aqui, você está tentando formatar uma mensagem, mas a chamada 'format()' está faltando argumentos.
        # Além disso, você não desempacotou os campos separados por vírgula corretamente.
        print('Nome {}, Idade {}'.format(registro.strip().split(',')))

finally:
    # Essa parte é executada independentemente de o bloco 'try' ter sucesso ou não.
    print('finally')

    # Aqui, você está tentando chamar o método 'close()' em uma string ('arquivo'), mas precisa chamá-lo no objeto 'arquivo'.
    # Além disso, você não precisa verificar se o arquivo está fechado, já que o bloco 'finally' garantirá que o arquivo seja fechado.
    arquivo.close()

# O bloco 'if' está fora do escopo do 'try', então 'arquivo' não está definido aqui.
# Além disso, essa verificação não é necessária, pois o bloco 'finally' já garante que o arquivo seja fechado.
if arquivo.closed:
    print("arquivo já fechado")
