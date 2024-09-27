op = 'S'
cont = 0
media = 0
maior = 0
menor = 0
while op == 'S':
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1
    media += n
    op = input('Quer continuar? [S/N] ').strip().upper()[0]
print(f'Você digitou {cont} números e a média foi {media/cont}\nO maior valor foi {maior} e o menor valor foi {menor}')