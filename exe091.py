from random import randint
from time import sleep
dados = dict()
lista = []
for c in range(4):
    dados["nome"] = f"jogador{c+1}"
    dados["valor"] = randint(1,6)
    lista.append(dados.copy())
    dados.clear()
for l in lista:
    print(f'O {l["nome"]} tirou {l["valor"]}')
    #sorted(dados, key=lambda d: d["valor"])
sorted(lista, key= lambda d: d["valor"])
for p, l in enumerate(lista):
    print(f'{p+1}º lugar: {l["nome"]} com {l["valor"]}')