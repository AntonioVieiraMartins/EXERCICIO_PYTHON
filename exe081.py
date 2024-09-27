numeros = list()
cont = 0
while True:
    numeros.append(int(input('Digite um número: ')))
    cont += 1
    if input('Quer continuar [S/N]? ') in 'nN':
        break
print(f'Total de números digitados {cont}')
numeros.sort(reverse=True)
print(numeros)
if 5 in numeros:
    print('O cinco foi digitado')
else:
    print('O cinco não foi digitado')