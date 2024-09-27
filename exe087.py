matriz = [[],[],[]]
spares = tcol = 0
for p,m in enumerate(matriz):
    for c in range(3):
        n = int(input(f'Digite um valor para [{p}, {c}]: '))
        matriz[p].append(n)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
for p,m in enumerate(matriz):
    for p1,m1 in enumerate(m):
        if p == 1:
            if p1 == 0:
                menor = m1
            elif menor > m1:
                menor = m1   
        if p1 == 2:
            tcol += m1
        if m1 % 2 == 0:
            spares += 1
        print(f'[ {m1} ]',end=' ')
    print()
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'A quantidde de valores pares é {spares}')
print(f'A soma dos valores da terceira coluna é {tcol}')
print(f'O menor valor da segunda coluna é {menor}')