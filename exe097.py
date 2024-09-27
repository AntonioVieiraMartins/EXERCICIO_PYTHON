def msg(msg):
    tamanho = len(msg)
    print('-'*tamanho)
    print(msg)
    print('-'*tamanho)


mensagem = input('Mensagem: ')
msg(mensagem)