maior = 0
menor = 0
for c in range(0,6):
    ano = int(input('Ano de nascimento: '))
    if 2024 - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'Foram contabilizados {maior} pessoas de maior e {menor} pessoas de menor')