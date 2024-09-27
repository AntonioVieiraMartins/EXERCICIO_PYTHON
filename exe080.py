numeros = list()
for c in range(5):
    numero = int(input('Digite um número: '))
    if c == 0:
        numeros.append(numero)
    else:
        for n in numeros:
            
print(numeros)