#Acessando listas dentro de lista


salas = [


['maria', 'carlos',], # vetor 0

['bruno', 'jose',], # vetor 1

['rafael', 'jonas', ], #vetor 2

[' sim', 'não', (0,10,20,30,40)], #vetor 3 tupla pode ser buscada pelo []

]



print (salas[3][2][2])



for sala in salas:
    for aluno in sala:
        print(aluno)