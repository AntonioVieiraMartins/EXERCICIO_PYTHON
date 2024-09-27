matriz = [[],[],[]]
for p,m in enumerate(matriz):
    for c in range(3):
        n = int(input(f'Digite um valor para [{p}, {c}]: '))
        matriz[p].append(n)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
for m in matriz:
    for m1 in m:
        print(f'[ {m1} ]',end=' ')
    print()