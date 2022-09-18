n = int(input())
lista = []

for i in range(0, n):
    bingus = []
    lista.append(bingus)
    for j in range(0, n):
        bingus.append(0)

l = n
k = 0
while l > 0 :
    for i in range(k,l):
        for j in range(k,l):
            lista[i][j] += 1
    l -= 1
    k += 1
for i in range(0,n):
    print(*lista[i])


