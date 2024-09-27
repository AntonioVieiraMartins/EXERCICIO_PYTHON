def maior(minha_lista):
    mai = 0
    for c in minha_lista:
        if c > mai:
            mai = c
    print(f'O maior valor é {mai}')

numeros = list()
cont = 0
while True:
    numeros.append(int(input(f'Número {cont+1}: ')))
    cont += 1
    if input('Quer continuar [S/N]? ') in 'Nn':
        break
maior(numeros)