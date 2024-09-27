n1 = float(input('Digite o primeiro número: '))
maior = n1
menor = maior
n2 = float(input('Digite o segundo número: '))
if n2 > maior:
    maior = n2
else:
    menor = n2
n3 = float(input('Digite o terceiro número: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print(f'O maior valor é {maior} e o menor valor é {menor}')
