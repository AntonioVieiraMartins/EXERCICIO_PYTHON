pessoas = list()
pessoa = []
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Nota 1: ')))
    pessoa.append(float(input('Nota 2: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    if input('Quer continuar [S/N]? ') in 'Nn':
      break
print(pessoas)
for c in range(len(pessoas)):
    print(f'{c}    {pessoas[c][0]}    {(pessoas[c][1]+pessoas[c][2])/2}')
while True:
   op = int(input('Mostrar a nota de qual aluno? (999)interrompe: '))
   if op == 999:
      break
   print(f'Notas de {pessoas[op][0]} são {pessoas[op][1]},{pessoas[op][1]}')