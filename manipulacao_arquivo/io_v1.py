# Abre o arquivo "pessoas.csv" no diretório atual para leitura.
arquivo = open('./pessoas.csv')

# Lê todo o conteúdo do arquivo e armazena na variável "dados".
dados = arquivo.read()

# Fecha o arquivo após ler o conteúdo.
arquivo.close()

# Inicia um loop para percorrer cada linha (registro) dos dados lidos.
for registro in dados.splitlines():
    # Divide cada registro em partes separadas pelo caractere ",".
    campos = registro.split(",")

    # Imprime uma mensagem formatada para cada registro.
    # O asterisco (*) antes de "registro.split(',')" desempacota os campos em argumentos separados.
    # Isso assume que cada registro tem exatamente dois campos: nome e idade.
    print('Nome: {}, Idade: {}'.format(*campos))
