
nome = "luiz otavio"

indice = 0

novo_nome = ''

while indice < len(nome): # len() retorna o tamanho da string, no caso, 11. Enquanto o tamanho do idice for menor que o tamanho da string, ele repetirá o laço
    letra = nome[indice] # letra recebe o valor do indice da string nome
    novo_nome += f'{letra}*' # novo_nome recebe o valor de novo_nome + letra + '*'
    indice += 1 # indice recebe o valor de indice + 1, ou seja, ele vai para o proximo indice da string nome adicionando O valor de letra + '*'

#novo_nome+= "*" # adiciona um '*' no final da string novo_nome, pois pela logica o indice não irá até o final da string nome
print(novo_nome)