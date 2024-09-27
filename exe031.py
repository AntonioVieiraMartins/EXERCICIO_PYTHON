km = float(input('Digite a distância da viagem em km: '))
if km > 200:
    print(f'O valor a pagar é {km * 2}')
else:
    print(f'O valor a pagar é {km * 1.5}')