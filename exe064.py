n = c = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        s += n
        c += 1
print(s,c)