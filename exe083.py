expre = input('Digite a expressão: ')
esq = dir = 0
for e in expre:
    if e == '(':
        esq += 1
    elif e == ')':
        dir += 1
if esq == dir:
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida')

#Ficou ótimo, pois o gustavo guanabara não explicou direito kkkk
#Depois fazer também caso alguém coloque ')(', pois isso retornará válido no código atual