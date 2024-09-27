tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break
print(f'Você digitou {tupla[num]}')