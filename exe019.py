import random
alu01 = input('Digite o nome do primeiro aluno: ')
alu02 = input('Digite o nome do segundo aluno: ')
alu03 = input('Digite o nome do terceiro aluno: ')
alu04 = input('Digite o nome do quarto aluno: ')
lista = [alu01, alu02, alu03, alu04]
random.shuffle(lista)
print(f'A ordem de apresentação será {lista}')