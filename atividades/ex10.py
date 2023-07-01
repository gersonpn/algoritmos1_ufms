linha = int (input())
colunas = int (input())
matriz = []


for i in range (0, linha+2):
    linha += 1
    matriz.append(linha)
print(matriz)

for j in range (linha, colunas+2):
    colunas += 1
    matriz.append(colunas)
print(matriz)
