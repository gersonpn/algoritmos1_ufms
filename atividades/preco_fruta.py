#As maçãs custam R$ 3  cada se forem compradas menos do que uma dúzia, e R$ 2,5 se forem compradas pelo menos doze.
#Com duas dúzias ou mais, é vendida no preço de atacado, R$1,75.
#Escreva um programa em Python  que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

fruta = int(input())

if fruta < 12:
    print(f" {fruta * 3:.2f}")
elif fruta >= 12 and fruta < 24:
    print(f"{fruta * 2.5:.2f}")
else:
    print(f" {fruta * 1.75:.2f}")
