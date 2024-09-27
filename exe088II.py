from random import randint
from time import sleep
jogo = list()
jogos = []
print('---------------------------------------')
print('          JOGA NA MEGA SENA')
print('---------------------------------------')
opc = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(opc):
    c = 0
    while True:
        n = randint(1,60)
        if n not in jogo:
            jogo.append(n)
            c += 1
        if c >= 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
print(f'=-=-=-= Sorteando {opc} jogos =-=-=-=')
for p,v in enumerate(jogos):
    sleep(1)
    print(f'Jogo {p+1}: {v}')
print('=-=-=-=-= Boa sorte! =-=-=-=-=')