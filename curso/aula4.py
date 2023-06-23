nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

print("Nome: ", nome, "\nIdade: ", altura, "\nPeso: ", peso, "\nIMC: ", imc)


#f string

print(f" Meu nome é {nome} e meu imc é {imc:.2f}")  #RETORNA Meu nome é João e meu imc é 25.00
print(f" Meu nome é {nome} e meu imc é {imc:,.2f}") #RETORNA Meu nome é João e meu imc é 25,000.000


# format


a = 10
b = 20
c = 30

lista = "a = {} b = {} c = {}"

formato = lista.format(a,b,c) # função format dentro do objeto formato que recebe a,b,c se transforma em um methodo

print(formato) #RETORNA a = 10 b = 20 c = 30
