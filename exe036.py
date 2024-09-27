casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o salário: '))
ano = int(input('Digite os anos para quitar: '))
mensal = casa/(ano * 12)
if mensal > sal * 30/100:
    print(f'Empréstimo negado parcela ({mensal:.2f})é maior que 30% da sua renda ({sal * 30/100:.2f})')
else:
    print('Empréstimo concedido')