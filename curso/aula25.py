
import os



lista = []

while True:
    opcao = input ("selecione uma opção: \n [i]nserir [a]pagar [l]istar: ")

    if opcao == 'i':
        os.system('cls')
        inseridos = input("Informe o item que deseja inserir: ")
        lista.append(inseridos)
        continue


    elif opcao == 'a':
        os.system('cls')
        apagar = input ("Escolha o indice que deseja apagar: ")

        try:
            indice = int(apagar)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')



    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
        for indice, nome in enumerate(lista):
            print(indice, nome)
        continue




    else:
        print ("Opção incorreta, digite novamente: ")