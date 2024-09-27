a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))
if a + b > c and a + c > b and b + c > a:
    print('É possivel formar um triângulo')
    if a == b and b == c:
        print('O triângulo formado é EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('O triângulo formado é ISOSCELES')
    else:
        print('O triângulo formado é ESCALENO')
else:
    print('Não é possível formar um triângulo')