def f_nota(notas, status=False):
    dici = {}
    dici["total"] = len(notas)
    dici["maior"] = max(notas)
    dici["menor"] = min(notas)
    dici["media"] = sum(notas)/len(notas)
    if status:
        if dici["media"] > 7:
            dici["situacao"] = 'boa'
        else:
            dici["situacao"] = 'ruim'
    print(dici)

notas = [7.8,8.9,7,9.8,5]
f_nota(notas, True)
print(notas)