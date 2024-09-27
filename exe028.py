from random import randint
npc = randint(0,5)
nusu = int(input('Digite um número entre 0 e 5: '))
if npc == nusu:
    print('Parabéns! Você acertou')
else:
    print(f'Que pena! A máquina escolheu {npc} e você {nusu}')