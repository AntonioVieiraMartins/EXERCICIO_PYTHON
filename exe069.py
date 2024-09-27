hom = p18 = m20 = 0
while True:
    print('----------------------------')
    print('    CADASTRE UMA PESSOA')
    print('----------------------------')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).strip().upper()[0]
    print('----------------------------')
    if idade > 18:
        p18 += 1
    if sexo in 'M':
        hom += 1
    if sexo in 'F' and idade < 20:
        m20 += 1
    op = input('Quer continuar? [S/N] ').upper()
    if op in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {p18}')
print(f'Ao todo temos {hom} homem cadastrados')
print(f'E temos {m20} mulheres com menos de 20 anos')