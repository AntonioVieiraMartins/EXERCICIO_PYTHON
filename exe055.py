maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'Digite o peso da pessoa {c} : '))
    if c == 1:
        maior = peso
        menor = maior
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(maior, menor)