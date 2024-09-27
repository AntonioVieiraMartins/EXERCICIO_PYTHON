from random import randint
cont = 0
print('=-'*19)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*19)
while True:
    op = int(input('Diga um valor: '))
    pc = randint(1,10)
    pi = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print('-------------------------------------')
    print(f'Você jogou {op} e o computador {pc}. Total deu {op+pc}')
    print('-------------------------------------')
    if pi in 'P':
        if (op + pc) % 2 == 0:
            print('Deu par. Você venceu')
        else:
            print('Deu ímpar. Você perdeu')
            break
    else:
        if (op + pc) % 2 != 0:
            print('Deu ímpar. Você venceu')
        else:
            print('Deu par. Você perdeu')
            break
    print('Vamos jogar novamente...')
    cont += 1
print(f'Você venceu {cont} vezes')
