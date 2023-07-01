a = float (input ())
b = float (input ())
c = float (input ())

if a + b < c or a + c < b or b + c < a:
    print('Não forma um triângulo')

else:
    if a == b and b == c and a == c:
        print('triângulo equilátero')
    elif a != b and b != c and a != c:
      print('triângulo escaleno')
    else:
        print('triângulo isósceles')