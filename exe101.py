def voto(year):
    ida = 2024 - year
    return ida

ano = int(input('Em que ano você nasceu? '))
idade = voto(ano)
if idade < 18:
    print(f'Com {idade} anos: Não vota.')
else:
    print(f'Com {idade} anos: Voto obrigatório.')