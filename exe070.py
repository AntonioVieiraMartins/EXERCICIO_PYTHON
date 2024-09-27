print('----------------------------')
print('    LOJA SUPER BARATÃO')
print('----------------------------')
tot = 0
mil = 0
while True:
    produt = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    if tot == 0: # Aqui daria para usar tot == 0 or preco < menor: daí apagaria o bloco elif
        menor = preco
        nomenor = produt
    elif preco < menor:
        menor = preco
        nomenor = produt
    tot += preco
    if preco > 1000:
        mil += 1
    op = input('Quer continuar? [S/N]').strip().upper()[0]
    while op not in 'SN':
        op = input('Opção inválida. Quer continuar? [S/N]').strip().upper()[0]
    if op not in 'S':
        break
print(f'O total da compra foi R${tot}')
if mil > 1:
    print(f'Temos {mil} produtos custando mais de R$1.000')
else:
    print(f'Temos {mil} produto custando mais de R$1.000')
print(f'O produto mais barato foi {nomenor}')