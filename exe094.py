pessoas = []
pessoa = {}
midade = 0
mulheres = []
while True:
    pessoa["nome"] = input('Nome: ')
    pessoa["sexo"] = input('Sexo [M/F]: ').upper()[0]
    pessoa["idade"] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    op = input('Quer continuar? [S/N]: ').upper()[0]
    if op in 'N':
        break
print('-='*32)
print(f'_ O grupo tem {len(pessoas)} pessoas')
for p in pessoas:
    for k, v in p.items():
        if k == 'idade':
            midade += v
        if k == 'sexo' and v == 'F':
            mulheres.append(p["nome"])
midade = midade/len(pessoas)
print(f'_ A média de idades é {midade}')
print('_ As mulheres cadastradas foram:',end=' ')
for c in mulheres:
    print(c, end=' ')
print()
print('_ Lista de pessoas acima da média: ')
for c in range(len(pessoas)):
    if pessoas[c]["idade"] > midade:
        print()
        print(f'Nome = {pessoas[c]["nome"]}; Sexo = {pessoas[c]["sexo"]}; Idade = {pessoas[c]["idade"]}')
print('<< ENCERRADO >>')