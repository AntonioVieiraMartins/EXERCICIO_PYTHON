valores = []
for c in range(5):
    valores.append(int(input(f'Digite o {c+1}º valor: ')))
print(max(valores))
print(min(valores))
print(valores.index(max(valores)))
print(valores.index(min(valores)))
