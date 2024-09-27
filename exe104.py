def leiaint(msg):
    while True:
        print(msg, end='')
        v = input()
        if v.isnumeric():
            break
        print('Erro! Digite um número inteiro válido.')
    return v
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')