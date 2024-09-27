numeros = (int(input('Valor 1: ')), int(input('Valor 2: ')), int(input('Valor 3: ')), int(input('Valor 4: ')))
pares = ()
for n in numeros:
    print(n, end=' ')
print(f'\nO valor 9 aparece {numeros.count(9)} vezes')
print(f'O valor 3 aparece pela primeira vez na posição {numeros.index(3)+1}')
print('Os valores pares são: ',end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
print('\nFim')