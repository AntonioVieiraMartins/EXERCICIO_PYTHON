palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'Na palavra {p} temos', end=' ')
    for p1 in p:
        if p1 in 'AEIOU':
            print(F'{p1}',end=' ')
    print('\n')