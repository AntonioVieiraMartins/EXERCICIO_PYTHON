fra = input('Digite uma frase: ').replace(' ','')
fra2 = fra[::-1]
if fra == fra2:
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é um palindromo')
