#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

n_estado = "scvd"
n_genero = "F ou M"



while True:

    nome = input("Digite o seu nome: ")
    if len(nome) < 3:
        nome = input("Nome incorreto, digite novamete: ")
        continue


    idade = int(input("Digite sua idade: "))
    if idade  < 0 or idade > 150:
        idade = float(input("incorreto, digite sua idade novamete: "))
        continue


    salario = int(input("Digite seu salario: "))
    if salario < 0:
        salario = input("salario incorreto, digite novamete: ")
        continue


    genero = input ("Digite seu genero: ")
    if genero.lower() not in n_genero.lower():
         genero = input("Digite o seu genero novamente: ")
         continue


    estado = input("Digite seu estado: ")
    if estado.lower() not in n_estado.lower():
        estado = input("Digite seu estado: ")
        continue





    print(f'seu nome é:  {nome}')
    print(f"sua idade é: {idade}")
    print(f"seu salario é: {salario}")
    print(f"Seu genero é: {genero}")
    print(f"seu estado é: {estado}")
    break