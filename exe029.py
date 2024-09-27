velo = float(input('Digite a velocidade do carro: '))
print(f'Sua velocidade é {velo}')
if velo > 80:
    print(f'Você foi multado. O valor da multa é {((velo-80)*28)}')
print('Ande com cuidado')
