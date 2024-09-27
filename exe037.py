n = int(input('Digite um número: '))
print('Escolha uma base para conversão')
print('[ 1 ] Converter para BINÁRIO\n[ 2 ] Converter em OCTAL\n[ 3 ] Converter em HEXADECIMAL')
opcao = int(input())
print(f'Opção {opcao} escolhida')
if opcao == 1:
    print(f'{n} em binário é {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} em ocatal é {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} em hexadecimal é {hex(n)[2:]}')
else:
    print('Nenhum valor válido escolhido')