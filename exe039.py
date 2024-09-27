ano = int(input('Ano de nascimento: '))
print(2016 - ano)
if 2016 - ano == 18:
    print('Você tem que se alistar esse ano (2016).')
elif 2016 - ano > 18:
    print(f'O seu alistamento foi há {2016 - (ano+18)} ano(s).\nVocê deveria ter se alistado em {ano + 18}')

else:
    print(f'Faltam {(ano + 18) - 2016} ano(os) para seu alistamento.\nVocê deverá se alistar em {ano + 18}')