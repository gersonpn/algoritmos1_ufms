def validar_n1():
        cpf = input("Escreva os 9 digitos do seu cpf: ")
        n = []
        new_cpf = []
        contagem = 10
        validar = 0
        
        for numero in str(cpf):
                n.append(int(numero))
                numero = int(numero) * contagem
                contagem -= 1
                new_cpf.append(numero)

        validar = sum(new_cpf) % 11

        if validar < 2:
                n.insert(11, 0)
        else:
                n.insert(11, 11 - (validar))

        return n


def validar_n2():

        novo_cpf = validar_n1()
        new_cpf = []
        n = []
        contagem = 11
        validar = 0

        for numero in novo_cpf:
                n.append(numero)
                numero = numero * contagem
                contagem -= 1
                new_cpf.append(numero)

        validar = sum(new_cpf) % 11

        if validar < 2:
                n.insert(11, 0)
        else:
                n.insert(11, 11 - (validar))

        return n




print(validar_n2())