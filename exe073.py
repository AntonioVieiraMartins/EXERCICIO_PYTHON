times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São paulo', 'Bahia', 'Vasco', 'Atlético MG', 'Internacional', 'Bragantino', 'Athletico PR', 'Criciúma', 'Juventude', 'Grêmio', 'Fluminense', 'Corinthians', 'Vitória', 'Cuiabá', 'Atlético GO')
print('=-=-=-=-= PRIMEIROS COLOCADOS =-=-=-=-=')
for c in range(5):
    print(f'{c+1}º {times[c]}')
print('=-=-=-=-= ÚLTIMOS COLOCADOS =-=-=-=-=')
for c in range(19, 15, -1):
    print(f'{c+1}º {times[c]}')
print('=-=-=-=-= ORDEM ALFABÉTICA =-=-=-=-=')
for C in sorted(times):
    print(F'{C} ')
print('O Fortaleza está na segunda colocação')