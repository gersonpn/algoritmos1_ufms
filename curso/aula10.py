# fatiamento de string usando a função len


#nome = str(input('Digite seu nome completo: ')).strip()#strip elimina os espaços antes e depois da string


nome = "olá mundo"


#fatiamento de string [inicio:fim:passo]

print (len(nome)) #len conta a quantidade de caracteres da string

print (nome[0:len(nome):2]) #imprime a string do inicio ao fim pulando de 2 em 2

