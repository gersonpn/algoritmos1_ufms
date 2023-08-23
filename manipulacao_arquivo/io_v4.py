# Abre o arquivo "pessoas.csv" no modo de leitura.
with open('pessoas.csv') as arquivo:
    # Loop que percorre cada linha (registro) do arquivo.
    for registro in arquivo:
        # Divide cada registro em campos separados por vírgula, removendo espaços em branco.
        campos = registro.strip().split(",")

        # Formata e imprime a mensagem para cada registro.
        print('Nome: {}, Idade: {}'.format(*campos))

# O bloco 'with' garante que o arquivo seja fechado automaticamente após a sua utilização.
# Portanto, a verificação de 'arquivo.closed' não é necessária aqui.
