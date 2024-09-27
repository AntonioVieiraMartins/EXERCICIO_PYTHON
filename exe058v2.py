from random import randint
print('''Sou seu computador...
Acabei de penser em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
pc = randint(0,10)
palpite = int(input('Qual seu palpite: '))
cont = 1
while pc != palpite:
    cont += 1
    if pc > palpite:
        print('mais... Tente mais uma vez.')
        palpite = int(input('Qual seu palpite: '))
    else:
        print('Menos... Tente novamente.')
        palpite = int(input('Qual seu palpite: '))
print(f'Acertou com {cont} tentativa. Parabéns!')