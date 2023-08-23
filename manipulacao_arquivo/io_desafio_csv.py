# Importa o módulo CSV para trabalhar com arquivos CSV.
import csv

# Importa a função 'request' do módulo 'urllib'.
# Isso permite realizar operações de solicitação HTTP, como baixar arquivos da web.
from urllib import request

# Define uma função chamada 'read' que recebe uma URL como parâmetro.
def read(url):
    # Abre a URL especificada no modo de leitura (HTTP GET request) usando 'request.urlopen()'.
    # O bloco 'with' garante que a conexão seja fechada corretamente após o uso.
    with request.urlopen(url) as entrada:
        print("Baixando arquivos...")

        # Lê os dados da resposta da requisição e os decodifica usando 'latin1'.
        # A decodificação é necessária para interpretar os bytes como caracteres legíveis.
        dados = entrada.read().decode('latin1')
        print("Arquivo baixado.")

        # O objeto 'csv.reader' interpreta os dados de forma que cada linha seja uma lista de campos.
        # Utiliza 'dados.splitlines()' para dividir os dados em linhas individuais.
        for cidade in csv.reader(dados.splitlines()):
            # Imprime a coluna 8 (nome da cidade) seguida da coluna 3 (UF) separadas por um espaço.
            print(f'{cidade[8]} {cidade[3]}')

# O bloco 'if __name__ == '__main__':' verifica se o script está sendo executado diretamente.
# Se for, chama a função 'read' com a URL especificada.
if __name__ == '__main__':
    # Chama a função 'read' e passa a URL do arquivo CSV como argumento.
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
