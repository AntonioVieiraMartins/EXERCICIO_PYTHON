def fatorial(valor, show=False):
    fat = 1
    for c in range(valor, 1, -1):
        fat *= c
        if show == True:
            if c > 2:
                print(c, end=' x ')
            else:
              print(c, end=' = ')  
    return fat

print(fatorial(7, True))