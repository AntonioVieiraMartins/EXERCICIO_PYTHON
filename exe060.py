n = int(input('Digite um número: '))
fat = 1
while n > 0:
    fat = n * fat
    n -= 1
print(fat)
