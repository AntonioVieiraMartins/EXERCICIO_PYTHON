from random import randint
npc = randint(0,5)
nusu = int(input('Digite um número entre 0 e 5: '))
if npc == nusu:
    print('Parabéns! Você acertou')
else:
    while npc != nusu:
        print(f'Que pena! A máquina escolheu {npc} e você {nusu}')
        npc = randint(0,5)
        nusu = int(input('Tente novamente. Digite um número entre 0 e 5: '))
    print('Parabéns! Você acertou')