n = int(input('Digite um número: '))
fat = 1
for c in range(n, 0, -1):
    fat = c * fat
print(fat)