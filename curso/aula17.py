senha_digitada = input("digite sua senha: ")
senha = '123456'


repeticao = 0

while senha_digitada != senha:
    senha_digitada = input ("senha incorreta digite novamente: ")
    repeticao +=1
    if repeticao > 1 and senha_digitada == senha:
      print(f"voce digitou a senha incorrte {repeticao}X")
print("senha correta")