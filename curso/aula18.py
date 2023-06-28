import os


palavra_secreta = "gato"
letra_acertadas = ""
repeticao = 0

while True:
    os.system('cls')
    
    letra_digitada = input ("Escreva uma letra: ") # entrada da letra

    if len(letra_digitada) > 1: # se letra maior que 1 caracter, pede para repetir novamente até ser == 1
        print("Digite uma letra de cada vez: ")
        repeticao +=1
        continue

    if letra_digitada not in palavra_secreta:
        print("Palavra errada, digite novamente")
        repeticao +=1
        continue


    if letra_digitada in palavra_secreta: # se letra_digitada estiver dentro da palavra secreta
        letra_acertadas += letra_digitada # será adicionado a letra acertada à letra digita

    palavra_formada = ''
    for letra_secreta in palavra_secreta: # para cada letra secreta, dentro da palavra secreta
        if letra_secreta in letra_acertadas: # se letra secreta in letra acertada, escreva a letra secreta descoberta
            palavra_formada += letra_secreta # letra secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)



    if palavra_formada == palavra_secreta:
        print("Parabéns, você acertou a palavra", {palavra_formada})
        print (f'você errou a palavra {repeticao}X')
        break
