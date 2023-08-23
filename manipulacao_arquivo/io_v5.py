# Abre o arquivo "pessoas.csv" no modo de leitura.
# O uso do bloco 'with' garante que o arquivo seja fechado automaticamente após sua utilização.
with open('pessoas.csv') as arquivo:
    # Abre o arquivo "pessoas.txt" no modo de escrita.
    # O segundo argumento 'w' indica que estamos abrindo o arquivo para escrita.
    # Também utilizamos o bloco 'with' para garantir o fechamento automático do arquivo.
    with open('pessoas.txt', 'w') as saida:
        # Loop que percorre cada linha do arquivo "pessoas.csv".
        for registro in arquivo:
            # Remove espaços em branco no início e no final da linha e, em seguida, divide os campos separados por vírgula.
            pessoa = registro.strip().split(',')

            # Formata uma mensagem contendo os valores do nome e idade da pessoa.
            # O uso de '*pessoa' desempacota os valores da lista 'pessoa' como argumentos individuais para 'format()'.
            # O parâmetro 'file=saida' indica que a mensagem será escrita no arquivo 'pessoas.txt'.
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

# Verifica se o arquivo 'arquivo' foi fechado após sair do bloco 'with'.
# Se o arquivo foi fechado, imprime a mensagem 'Arquivo fechado'.
# No entanto, essa verificação não é necessária, pois o bloco 'with' fecha automaticamente os arquivos.
if arquivo.closed:
    print('Arquivo fechado')
