n = int(input("escreva um valor: "))

vetor = []


for item in range(n):
    var = [] #0

    for valor in range(item,item+n):
        valor+=1 #0+1
        var.append(valor) #1
    vetor.append(var) # [1,2,3]



for linha in vetor:
    print(linha)
