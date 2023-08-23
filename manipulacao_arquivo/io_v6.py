# Importa o módulo CSV, que fornece funcionalidades para lidar com arquivos CSV.
import csv

# Abre o arquivo "pessoas.csv" no modo de leitura.
with open('pessoas.csv') as entrada:
    # Loop que percorre cada linha (registro) do arquivo utilizando o csv.reader().
    # O csv.reader() interpreta cada linha como uma lista de campos.
    for pessoa in csv.reader(entrada):
        # A linha lida é considerada uma lista de campos separados por vírgula.
        # Utilizamos o desempacotamento '*' para formatar e imprimir a mensagem.
        print('Nome: {}, Idade: {}'.format(*pessoa))
