import random
from time import sleep
jogos = list()
jogo = list()
print('---------------------------------------')
print('          JOGA NA MEGA SENA')
print('---------------------------------------')
op = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-=-= Sorteando {op} jogos =-=-=-=')
for c in range(op):
    #jogo = list() colocando aqui não há necessidade de fazer o clear e [:]
    for c in range(6):
        if c == 0:
            n = random.randint(1,99)
            jogo.append(n)
        else:
            while True:
                n = random.randint(1,99)
                for j in jogo: # essa parte não ficou 100%
                    if n == j:
                        n = random.randint(1,99)
                        break
                jogo.append(n)
                break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
for c in range(len(jogos)):
    sleep(1)
    print(f'Jogo {c+1}: {jogos[c]}')
sleep(1)
print('=-=-=-=-= Boa sorte! =-=-=-=-=')