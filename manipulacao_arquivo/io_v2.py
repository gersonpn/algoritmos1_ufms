# Abre o arquivo "pessoas.csv" no modo de leitura.
arquivo = open('pessoas.csv')

# Loop que percorre cada linha (registro) do arquivo.
for registro in arquivo:
    # Divide cada registro em campos separados por vírgula e remove espaços em branco.
    campos = registro.strip().split(',')

    # Formata e imprime a mensagem para cada registro.
    print('Nome: {} Idade: {}'.format(*campos))

# Fecha o arquivo após a leitura.
arquivo.close()
