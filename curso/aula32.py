n = input("Escreva seu CPF: ")
cpf =[ int(digito) for digito in str(n)]
contagem = 11
new_cpf = []

while len(cpf) != 11:
    n = input("errado, Escreva seu CPF: ")
    cpf =[ int(digito) for digito in str(n)]



for numero in cpf[0:9]:
    contagem -= 1
    numero *= contagem
    new_cpf.append(numero)


soma_dig_1 = sum(new_cpf)
div_1 = soma_dig_1 // 11

if div_1  == 2:
    
