print('========================================')
print('               BANCO M&W')
print('========================================')
vl = int(input('Que valor você quer sacar? R$'))
c50 = c20 = c10 = c1 = 0
if vl >= 50:
    c50 = vl //50
    vl = vl % 50
    print(f'Total de {c50} cédulas de 50')
if vl >= 20:
    c20 = vl //20
    vl = vl % 20
    print(f'Total de {c20} cédulas de 20')
if vl >= 10:
    c10 = vl //10
    vl = vl % 10
    print(f'Total de {c10} cédulas de 10')
if vl >= 1 and vl < 10:
    c1 = vl * 1
    print(f'Total de {c1} cédulas de 1')
print('========================================')
print('Volte sempre')
