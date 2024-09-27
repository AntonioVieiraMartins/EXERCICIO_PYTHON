numeros = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    if input('Quer continuar [S/N]? ') in 'Nn':
        break
pares = list()
impares = list()
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Lista completa {numeros}')
print(f'Lista com pares {pares}')
print(f'Lista com ímpares {impares}')