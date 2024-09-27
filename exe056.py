media = 0
h_m = ' '
c_m = 0
maior_idade = 0
for c in range(4):
    print(f'-------- {c+1}ª pesoa --------')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    media += idade
    sexo = input('Sexo[M/F]: ').strip().upper()[0]
    if sexo == 'M' and idade > maior_idade:
        h_m = nome
        maior_idade = idade
    if sexo == 'F' and idade < 21:
        c_m += 1
print(f'A média de idade do grupo é de {media/4} anos')
print(f'O Homem mais velho tem {maior_idade} e se chama {h_m}')
print(f'Ao todo são {c_m} mulheres com menos de 21')