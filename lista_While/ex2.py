#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.


nome = input("Digite seu nome:")
senha = input("Digite sua senha:")


while nome == senha:
    senha = input("Erro! Nome e senha iguais, digite uma nova senha: ")

else:
    print("Nome e senha diferentes, cadastro realizado com sucesso!")
