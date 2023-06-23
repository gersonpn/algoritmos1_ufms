#operadores logicos and, or, not


#and - verdadeiro se as duas condições forem verdadeiras
#or - verdadeiro se uma das condições for verdadeira
#not - inverte o valor da condição

entrada = input("Digite um valor: ")

verdadeiro = True
falso = False



if entrada == "sim" or entrada == "s":
    print("Sim")

elif entrada == "não" or entrada == "n":
    print("Não")

else:
    print("Nada")




#not - inverte o valor da condição


idade = int(input("Digite sua idade: "))

if not idade == 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# operadores in e not in

# in - verifica se um valor está contido em uma lista
# not in - verifica se um valor não está contido em uma lista


lista = [1, 2, 3, 4, 5]


if 3 in lista:
    print("3 está na lista")



if 9 not in lista:
    print("9 não está na lista")