jogador = dict()
gols = []
jogador["nome"] = input('Nome do jogador: ')
partida = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(partida):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador["gols"] = gols
jogador["total"] = sum(gols)
print('=-'*30)
print(jogador)
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {partida} partidas')
for c in range(len(gols)):
    print(f'    => Na partida {c}, fez {gols[c]}')
print(f'Foi um total de {jogador["total"]} gols')