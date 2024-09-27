pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
c = 10
while c > 0:
    print(f'{pri}',end=' > ')
    c -= 1
    pri += raz
print('Fim')