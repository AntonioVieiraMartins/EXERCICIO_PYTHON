soma = 0
cont = 0
for c in range(0,6):
    n = int(input(f'Digite o {c + 1} número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você entrou com {cont} números pares e a soma foi {soma}')