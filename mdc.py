n = int(input())
numeros = input().split()

for i in range(0, n):
    numeros[i] = int(numeros[i])

cond1 = False
cond2 = False

if 2 <= n and n <= 1e5 :
    cond1 = True

for i in range(0,n):
    if 1 <= numeros[i] and numeros[i] <= 1e6 :
        cond2 = True
    else:
        cond2 = False
        break

if cond1 and cond2 :
    inicio = min(numeros)
    while True:
        bingus = False
        for i in range(0,n):
            if numeros[i] % inicio == 0 :
                bingus = True
            else:
                bingus = False
                break
        if bingus :
            break
        inicio -= 1
    print(inicio)