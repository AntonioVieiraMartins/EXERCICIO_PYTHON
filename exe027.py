nome = input('Digite seu nome completo: ')
print(nome[:nome.find(' ')])
print(nome[nome.rfind(' ')+1:])