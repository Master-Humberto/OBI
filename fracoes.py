from sympy import denom


numeros = input().split()
a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])
d = int(numeros[3])

cond1 = False
cond2 = False
cond3 = False
cond4 = False

if 1 <= a and a <= 1e8:
    cond1 = True

if 1 <= b and b <= 1e8:
    cond2 = True

if 1 <= c and c <= 1e8:
    cond3 = True

if 1 <= d and d <= 1e8:
    cond4 = True

if cond1 and cond2 and cond3 and cond4 :
    # a/b + c/d
    numerador = a*d + b*c
    denominador = b*d
    lista = []
    lista.append(numerador)
    lista.append(denominador)
    print(*lista)
    