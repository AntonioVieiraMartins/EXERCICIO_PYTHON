numeros = []
while True:
    numero = int(input('Digite um número: '))
    if len(numeros) == 0:
        numeros.append(numero)
    else:
        c = 0
        for n in numeros: # Guanabara usou not in com if kkkk 
            if n == numero:
                c += 1
        if c == 0:
            numeros.append(numero)
        else:
            print('Número já existe')
    if input('Quer continuar? [S/N] ') not in 'Ss':
        break
numeros.sort()
print(numeros)