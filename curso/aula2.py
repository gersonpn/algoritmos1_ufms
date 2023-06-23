#variaveis
nome = "Rafael"
idade = 30
maior_idade = idade >= 18
print("Nome: ", nome, "\nIdade: ", idade, "\nMaior de idade: ", maior_idade) #\n quebra de linha

#operadores aritmeticos
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3) #divisão RETORNA float
print(9.25 // 3.5) #divisão inteira RETORNA
print(2 ** 3) #potencia
print(25 % 3) #resto da divisão RETORNA 0 OU 1

#operadores relacionais
print(2 > 3) #RETORNA True ou False maior que
print(2 < 3) #RETORNA True ou False menor que
print(2 >= 3) #RETORNA True ou False maior ou igual
print(2 <= 3) #RETORNA True ou False menor ou igual
print(2 == 3) #RETORNA True ou False igual
print(2 != 3) #RETORNA True ou False diferente


#operadores logicos

#and
print(True and True) #RETORNA True
print(True and False) #RETORNA False
print(False and True) #RETORNA False
print(False and False) #RETORNA False

#or
print(True or True) #RETORNA True
print(True or False) #RETORNA True
print(False or True) #RETORNA True
print(False or False) #RETORNA False

#not
print(not True) #RETORNA False
print(not False) #RETORNA True

#operadores de atribuição
x = 2
x = x + 3
print(x)
x += 3 #x = x + 3
print(x)
x -= 3 #x = x - 3
print(x)
x *= 3 #x = x * 3
print(x)
x /= 3 #x = x / 3
print(x)
x //= 3 #x = x // 3
print(x)
x **= 3 #x = x ** 3
print(x)
x %= 3 #x = x % 3
print(x)

#operadores de identidade
x = 3
y = 3
print(x is y) #RETORNA True se x e y forem o mesmo objeto
print(x is not y) #RETORNA False se x e y forem o mesmo objeto

#operadores de membro
x = "Rafael"
print("R" in x) #RETORNA True se R estiver em x
print("R" not in x) #RETORNA False se R estiver em x

#operadores ternarios
idade = 18
print("Maior de idade" if idade >= 18 else "Menor de idade") #RETORNA Maior de idade se idade >= 18, senão retorna Menor de idade

#operadores bitwise
# 5 = 00000101
# 4 = 00000100
# 3 = 00000011


