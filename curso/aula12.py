#try/except


numero = input('Digite um número: ')

try: #valida se o que foi digitado é um número, transforma a string em um numero e apresenta a multiplicação
    print ("O número digitado foi: ", numero)
    numero_float = float(numero)
    print ("O número digitado foi: ", numero_float)
    print (f"o dobro de {numero} é {numero_float * 2}")

except: #caso o que foi digitado não seja um número, apresenta a mensagem de erro dentro do try e executa o execpt, printando que não é o número
    print ("isso não é um número")