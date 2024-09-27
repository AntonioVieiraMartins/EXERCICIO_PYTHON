op = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while op != 5:
    if op == 4:
        print('Digite os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    op = int(input('>>>>>> Qual é a sua opção? '))
    if op not in(1,2,3,4,5):
        print('Opção inválida. Tente novamente')
    if op == 1:
        print(n1 + n2)
    elif op == 2:
        print(n1 * n2)
    elif op == 3:
        if n1 > n2:
            print(f'{n1} > {n2}')
        else:
            print(f'{n2} > {n1}')
print('Fim')