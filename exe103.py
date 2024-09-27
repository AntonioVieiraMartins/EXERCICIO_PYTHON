def jogador(nome, gols):
    print('-----------------------------------------------------')
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')
nome = input('Jogador: ')
if nome =='' or nome in ' ':
    nome = '<Desconhecido>'
gol = (input('Gols: '))
if gol == '' or gol in ' ':
    gol = int(0)
else:
    gol = int(gol)
jogador(nome=nome, gols=gol)