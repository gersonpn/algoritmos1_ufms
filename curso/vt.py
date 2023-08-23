import random

print("Bem-Vindo ao Jogo")

random.randint(0,100)

tentativa = 1

numero_tentativas = 0

numero_correto = 3

n = 0

print("Determine a Dificuldade: (1)Fácil (2)Médio (3)Difícil")

modo = int(input("Modo Escolhido: "))

chute = int(input("Escolha seu valor : "))

if(modo == 1):
    numero_tentativas = 20

elif(modo == 2):
    numero_tentativas = 10

elif(modo == 3):
    numero_tentativas = 5


while n < numero_tentativas:

    n += 1

    if(chute == numero_correto):
        print("Parabéns, Você Acertou!")
        break

    elif(chute > numero_correto):
        print("Está Errado, Tente um valor menor!")
        chute = int(input("Escolha seu valor : "))
        continue

    elif(chute < numero_correto):
        print("Está Errado, Tente um valor maior!")
        chute = int(input("Escolha seu valor : "))
        continue

print("TENTATIVAS ESGOTADAS ")
