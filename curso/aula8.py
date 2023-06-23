#interpolação

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print('Olá %s, você tem %d anos' % (nome, idade)) # %s - string, %d - inteiro, dessa forma é possível interpolar variáveis dentro de uma string


#transformação de hexadecimal

numero = int(input("Digite um número: "))

print ("O número %d em hexadecimal é %08X" % (numero, numero)) # %x - hexadecimal ou %X - hexadecimal em maiúsculo caso deseje completar o hexadecimal com zeros basta colocar 0 antes do x ou X, exemplo: %08x ou %08X