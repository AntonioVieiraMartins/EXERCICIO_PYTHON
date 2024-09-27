from random import randint
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados foram:', end= ' ')
for n in tupla:
    print(f'{n}',end= ' ')
maior = sorted(tupla)
print(f'\nO maior valor sorteado foi {maior[4]}')
print(f'O menos valor sorteado foi {maior[0]}')
#Poderia ter usado max e min para pegar o maior e menos valor na tupla