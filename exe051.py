pri = int(input('Primeiro termo da P.A: '))
raz = int(input('Razão da P.A: '))
cont = pri
print(cont)
for c in range(pri, 9):
    cont += raz
    print(f'{cont}', end=' -> ')
print('ACABOU')