pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
cont = 0
c = 10
while c !=  0:
    while c > 0:
        print(f'{pri}',end=' > ')
        c -= 1
        pri += raz
        cont += 1
    print('Pausa')
    c = int(input('Quantos termos quer mostrar a mais? '))
print(f'Progreção finalizada com {cont} termos mostrados.')
