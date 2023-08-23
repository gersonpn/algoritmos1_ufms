def validar_n1():
        cpf = input("Escreva os 9 digitos do seu cpf: ")
        new_cpf = []
        cpf = list(cpf)
        contagem = 11

        for numero in cpf [0:9]:
                contagem -= 1
                numero *= contagem
                new_cpf.append(numero)

        print(new_cpf)

        return cpf

print(validar_n1)