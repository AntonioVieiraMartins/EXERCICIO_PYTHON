from time import sleep
def tipo1():
    for c in range(1, 11):
        print(c,end=' ')
        sleep(1)
    print()

def tipo2():
    for c in range(10, -1, -2):
        sleep(1)
        print(c, end=' ')
    print()

def contador(start, end, step):
    for c in range(start, end + 1, step):
        sleep(1)
        print(c, end=' ')
    print()

tipo1()
tipo2()
print('Agora é sua vez de personalizar a contagem')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)