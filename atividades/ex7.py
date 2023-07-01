vetor = int(input())
lista = []

for linha in range(vetor):
    vt = []
    for coluna in range(linha, linha+vetor):
        coluna+= 1
        vt.append(coluna)
    linha.append(vt)

for linha in vetor:
    print(linha)
