lista = ('Leite', 4, 'Ovo', 12, 'Frango', 7, 'Carne', 30, 'Feijão', 5, 'Nescal', 7)
print('-----------------------------')
print('     LISTAGEM DE PREÇOS')
print('-----------------------------')
for c in range(len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]}',end='..................')
        print(f'R$ {lista[c+1]}\n')

