t = int(input('Quantos termos você quer mostrar? '))
c = n1 = 0
n2 = 1
while t > 0:
    if c == 0:
        print(n1)
        print(n2)
    else:
        soma = n1 + n2
        print(soma)
        n1 = n2
        n2 = soma
    t -= 1
    c += 1