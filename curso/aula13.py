n = input ("Digite um número: ")

if n.isdigit(): #valida se o que foi digitado é um número inteiro, transforma a string em um numero inteiro e apresenta se é par ou impar
    n_inteiro = int(n)
    if n_inteiro % 2 == 0:
        print (f"O número {n_inteiro} é par")
    else:
        print (f"O número {n_inteiro} é impar")
else:
    print ("Você não digitou um número inteiro")