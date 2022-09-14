t = int(input())

while t > 0 :
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    dic = {}
    for i in range(0, m):
        a = input()
        b = input()
        dic[a] = b 
    #### ta funcionando 
    lista_dicionario = list(dic.keys())

    for i in range(0,n):
        x = input().split()
        lista = []
        for j in range(0, len(x)):
            if x[j] in lista_dicionario:
                lista.append(dic[x[j]])
            else:
                lista.append(x[j])

        print(*lista)
        
    print()
    t -= 1

    