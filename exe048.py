soma = 0
cont = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        #print(c)
        soma = c + soma
        # soma += c
        cont = cont + 1
        # cont += 1
print(f'A soma dos {cont} números solicitados é {soma}')
