
frase = "aaaaoooo"

i = 0

qtd_letras = 0

letra_mais_repetida = ""


while i < len (frase): # enquanto o i for menor que o tamanho da frase
    letra_atual = frase[i] # adiciona a letra uma por uma na variavel letra_atual

    if letra_atual == " ": # se a letra atual for igual a um espaço
        i += 1 # adiciona mais um ao i
        continue #repita o loop

    qtd_letras_atual = frase.count(letra_atual) # conta quantas vezes a letra atual aparece na frase

    if qtd_letras  < qtd_letras_atual: # se a quantidade de letras for menor que a quantidade de letras atual
        qtd_letras = qtd_letras_atual # a quantidade de letras recebe a quantidade de letras atual
        letra_mais_repetida = letra_atual # a letra mais repetida recebe a letra atual



    i += 1 # adiciona mais um ao i

print("A letra mais repetida é: ", letra_mais_repetida) 