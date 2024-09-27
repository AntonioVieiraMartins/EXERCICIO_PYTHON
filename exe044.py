print('============= LOJAS VIEIRA =============')
preco = float(input('Valor das compras: '))
print('FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
opcao = int(input('Opção: '))
if opcao == 1:
    print(f'O valor a pagar é {preco - preco * 0.1}')
elif opcao == 2:
    print(f'O valor a pagar é {preco - preco * 0.05}')
elif opcao == 3:
    print(f'O valor a pagar é {preco}')
elif opcao == 4:
    print(f'O valor a pagar é {preco + preco * 0.2}')
else:
    print('Nenhuma opção escolhida. Tente novamente')