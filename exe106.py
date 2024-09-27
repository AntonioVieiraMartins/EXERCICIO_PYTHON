def ajuda(func):
    help(func)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('       SISTEMA DE AJUDA HEP')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
while True:
    op = input('Sistema ou biblioteca: ')
    if op == 'quit':
        break
    ajuda(op)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('-=-=-=-')
