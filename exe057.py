'''sexo = input('Sexo [M/F]: ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite novamente. O sexo deve ser [M/f]: ')'''


sexo = input('Sexo [M/F]: ').upper()
while sexo not in 'MmFf':
    sexo = input('Digite novamente. O sexo deve ser [M/f]: ')