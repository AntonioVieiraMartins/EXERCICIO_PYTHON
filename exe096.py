def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é {area}m².')


print('Controle de terrenos')
print('-------------------')
larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
area(larg, comp)