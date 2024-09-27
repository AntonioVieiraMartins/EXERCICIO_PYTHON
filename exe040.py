n1 = float(input('Nota 01: '))
n2 = float(input('Nota 02: '))
media = (n1 + n2) / 2
if media < 5:
    print('Reprovado!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')