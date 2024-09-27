pessoa = dict()
pessoa["nome"] = input('Nome: ')
pessoa["idade"] = 2024 - int(input('Ano de nascimento: '))
pessoa["ctps"] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa["ctps"] != 0:
    pessoa["contratacao"] = int(input('Ano de contratação: '))
    pessoa["salario"] = float(input('Salário: R$'))
    pessoa["aposentadoria"] = pessoa["contratacao"] + 35
for k,v in pessoa.items():
    print(f'{k} tem o valor de {v}')