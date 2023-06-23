#estruturas condicionais if, elif, else

entrada = input ("Você quer entrar ou sair: ")


if entrada == "entrar":
    print("Bem vindo ao sistema")

elif entrada == "sair":
    print("Obrigado por usar nosso sistema")

else:
    print("Você não digitou uma opção válida")



condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False

if condicao1:
    print("condicao1 é verdadeira")
elif condicao2:
    print("condicao2 é verdadeira")
elif condicao3:
    print("condicao3 é verdadeira")
elif condicao4:
    print("condicao4 é verdadeira")

else:
    print("nenhuma condição é verdadeira")
