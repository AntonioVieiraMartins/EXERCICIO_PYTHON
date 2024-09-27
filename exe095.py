jogadores = []
print('--------------------------------------')
while True:
    jogador = dict()
    gols = []
    jogador["nome"] = input('Nome do jogador: ')
    partida = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    jogador["partida"] = partida
    for c in range(partida):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador["gols"] = gols
    jogador["total"] = sum(gols)
    jogadores.append(jogador.copy())
    op = input('Quer continuar [S/N]? ')
    if op in 'Nn':
        break
    print('--------------------------------------')
print('-='*20)
for c in range(len(jogadores)):
    print(f'{c} - {jogadores[c]["nome"]} {jogadores[c]["gols"]} {jogadores[c]["total"]}')
while True:
    op = int(input('Mostrar levantamento de qual jogador? '))
    if op == 999:
        break
    print('--------------------------------------')
    print(f'O jogador {jogadores[op]["nome"]} jogou {jogadores[op]["partida"]} partidas')
    for c in range(len(jogadores[op]["gols"])):
        print(f'    => Na partida {c}, fez {jogadores[op]["gols"][c]}')
    print(f'Foi um total de {jogadores[op]["total"]} gols')
print('<< VOLTE SEMPRE >>')