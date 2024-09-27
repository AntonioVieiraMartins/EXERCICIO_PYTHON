galera = list()
pessoa = [] # n precisa dessas duas listas kkk é só printar
ppesadas = []
pleves = []
contp = 0
maior = menor = 0
while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    if contp == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    pessoa.append(nome)
    pessoa.append(peso)
    galera.append(pessoa[:])
    pessoa.clear()
    contp += 1
    if input('Quer continuar [S/N]? ') in 'Nn':
        break
print(f'Ao todo você cadastrou {contp} pessoas')
for p in galera:
    if p[1] == maior:
        ppesadas.append(p[0][:])
    if p[1] == menor:
        pleves.append(p[0][:])
print(f'O maior peso foi {maior} kg. Peso de {ppesadas}')
print(f'O menor peso foi {menor} kg. Peso de {pleves}')