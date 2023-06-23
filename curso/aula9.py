#formatação de string
# > - alinhamento a direita
# < - alinhamento a esquerda
# ^ - alinhamento centralizado
# : - formatação
# 0 - preenchimento com zero
# , - separador de com virgula
# _ - separador com underline
# . - separador com ponto
# b - binário
# o - octal
# x - hexadecimal
# f - float
# e - float exponencial
# :.2f - duas casas decimais
# :.2% - duas casas decimais e porcentagem
# :.2e - duas casas decimais e exponencial
# :.2x - duas casas decimais e hexadecimal
# :.2o - duas casas decimais e octal
# :.2b - duas casas decimais e binário
# :.2_ - duas casas decimais e separador com underline
# :.2, - duas casas decimais e separador com virgula
# :.2$ - duas casas decimais e separador com cifrão
# :.2f - duas casas decimais e float
# :.2f - duas casas decimais e float
# :.2f - duas casas decimais e float
# :.2f - duas casas decimais e float
# :.2f - duas casas decimais e float
# :.2f - duas casas decimais e float
# :.2f - duas casas decimais e float
# :.2f - duas casas decimais e float
# :.2f - duas casas decimais e float



nome = input ('Digite seu nome: ')

numero = int(input('Digite um número: '))


print (f'{nome: >10}') # : >10 - alinhamento a direita com 10 espaços
print (f'{nome: <10}') # : <10 - alinhamento a esquerda com 10 espaços
print (f'{nome: ^10}') # : ^10 - alinhamento centralizado com 10 espaços


print (f'{numero:0>10}') # :0>10 - alinhamento a direita com 10 espaços e preenchimento com zero
print (f'{numero:0<10}') # :0<10 - alinhamento a esquerda com 10 espaços e preenchimento com zero
print (f'{numero:0^10}') # :0^10 - alinhamento centralizado com 10 espaços e preenchimento com zero

print (f'{numero: b}')
print (f'{numero: o}')
print (f'{numero:08X}')
print (f'{numero: f}')
