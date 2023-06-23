nome = input("Escreva seu nome: ")

idade = input("Escreva sua idade: ")


if nome and idade != "":
      print(f"Seu nome é: {nome}")
      print(f"seu nome invertido é: {nome[::-1]}")
      print (f"seu nome contem {len(nome)} letras")
      
      if " " in nome: #verifica se existe espaço na string
            print ("Seu nome contem espaços")
      else:
            print ("Seu nome não contem espaços")
      print (f" a primeira letra do seu nome é {nome[0]}")
      print (f" a ultima letra do seu nome é {nome[-1]}")
else:
      print ("Você não digitou um nome válido")
