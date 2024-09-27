sal = float(input('Digite o seu salário: '))
if sal >= 4500:
    sal = sal + sal * 30/100
else:
    sal = sal + sal * 35/100
print(f'Seu salário novo é {sal}')