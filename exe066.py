c = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    soma += n
print(c, soma)