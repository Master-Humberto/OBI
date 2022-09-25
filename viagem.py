cond1 = False
cond2 = False
cond3 = False
cond4 = False
cond5 = False
cond6 = False
cond7 = False
cond8 = False 
vnm = input().split()
v = int(vnm[0])
n = int(vnm[1])
m = int(vnm[2])
if 2 <= n and n <= 10000:
    cond1 = True
if 1 <= m and m <= 2000:
    cond2 = True
if 1 <= v and v <= 200:
    cond3 = True
grafo = []
grafo_djikstra = []
caminhos = []
for i in range(0, m):
    x = input().split()
    ai = int(x[0])
    bi = int(x[1])
    ti = int(x[2])
    pi = int(x[3])
    grafo.append([ai,bi,ti,pi])
    grafo.append([bi,ai,ti,pi])
    if 1 <= ai and ai <=n and 1 <= bi and bi <= n and 1 <= ti and ti <= 100000 and 0 <= pi and pi <= 200:
        cond4 = True
        cond5 = True
        cond6 = True
        cond7 = True
    else:
        cond4 = False
        cond5 = False
        cond6 = False
        cond7 = False
        cond8 = False
        break
trajeto = input().split()
inicial = int(trajeto[0]) - 1
final = int(trajeto[1]) - 1

if 1 <= (inicial+1) and (inicial+1) <= n and 1 <= (final+1) and (final +1)<= n :
    cond8 = True
## LINE BREAKER Construtor do problema
if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7 and cond8:

    matriz_precos= []
    grafao = []
    bingus = []

    for i in range(0, n):
        for j in range(0,n):
            bingus.append(0)

        grafao.append(bingus)
        bingus = []

    changus = []
    for i in range(0,n):
        for j in range(0,n):
            changus.append(0)

        matriz_precos.append(changus)
        changus = []
    #print(grafao)
    # Construtor do grafao

    for i in range(0, len(grafo)):
        matriz_precos[grafo[i][0]-1][grafo[i][1]-1] = grafo[i][3]

    for i in range(0,len(grafo)):
        grafao[grafo[i][0]-1][grafo[i][1]-1] = grafo[i][2]

    # print(grafao)
    # print(matriz_precos)

    #### LINE BREAKER Construtor do Grafo
    run = True
    class ShortestPathAnd2ndShortestDijkstras:
        NO_PARENT = -1	
        path = []; #nodes in the shortest path
        allDists = set(); #list of shortest distance
        lista_de_precos = []; # lista de precos
        paths = []
        #use Dijkstra’s Shortest Path Algorithm, O(n^2) Space O(n)
        def shortestPath(self, adjacencyMatrix,matriz_precos,  src, dest, run) : 
            n = len(adjacencyMatrix[0]) 
            preco = 0
            shortest = {}
            visited = {}
            parents = {}
            dic_precos = {}
            for v in range(0, n, 1)  :
                shortest[v] =  1e10 
                dic_precos[v] = 1e10
                visited[v] = False
            shortest[src] = 0; 
            dic_precos[src] = 0; 
            parents[src] = self.NO_PARENT; 
            for i in range(1, n, 1) : 
                pre = -1; 
                min =  1e10; 
                preco_minimo = 1e10
                for v in range(0, n, 1) : 
                    if visited[v]==False and shortest[v] < min:
                        pre = v; 
                        min = shortest[v]; 
                        preco_minimo = dic_precos[v]; 
                if pre == -1:
                    run = False
                    return run
                visited[pre] = True; 
                for v in range(0, n, 1)  : 
                    dist = adjacencyMatrix[pre][v];    
                    valor = matriz_precos[pre][v]              
                    if dist > 0 and ((min + dist) < shortest[v]) :   
                        parents[v] = pre
                        shortest[v] = min + dist 
                        dic_precos[v] = preco_minimo + valor 
                        
                        
                        
                    

            try:
                self.allDists.add(shortest[dest])
                self.addPath(dest, parents); 
                self.lista_de_precos.append(dic_precos[dest])
            except KeyError:
                run = False
                return run 
        
        #utility func to add nodes in the path recursively
        def addPath(self, i, parents) : 	
            if (i == self.NO_PARENT) :
                return  	
            self.addPath(parents[i], parents)             
            self.path.append(i) 
        #get 2nd shortest by removing each edge in shortest and compare  
        def find2ndShortest(self, adjacencyMatrix,precos, src, dest, run) : 
            #store previous vertex's data  	
            preV = -1
            preS = -1 
            preD = -1 
            mylist = list(self.path)       
            for i in range(0, len(mylist)-1, 1) :
                #get source and destination for each path in shortest path
                s = mylist[i]
                d = mylist[i + 1]
                #resume the previous path 
                if (preV != -1) :
                    adjacencyMatrix[preS][preD] = preV
                    adjacencyMatrix[preD][preS] = preV       
                #record the previous data for recovery
                preV = adjacencyMatrix[s][d]
                preS = s
                preD = d
                #remove this path
                adjacencyMatrix[s][d] = 0
                adjacencyMatrix[d][s] = 0
                #re-calculate
                self.shortestPath(adjacencyMatrix,precos, src, dest, run)

    myobj = ShortestPathAnd2ndShortestDijkstras()

    i = 0
    run = True
    caminhos = []
    lista_precos = []
    distancias = []
    while run : 
        if i == 0: 
            myobj.shortestPath(grafao, matriz_precos, inicial, final, run)
        else:
            myobj.find2ndShortest(grafao,matriz_precos,inicial,final, run)

        try:
            distancias.append(list(myobj.allDists)[i])
            lista_precos.append((myobj.lista_de_precos[i]))
        except IndexError:
            run = False
        i += 1

    bingus = False 

    for i in range(0, len(lista_precos)):
        if lista_precos[i] <= v : 
            print(distancias[i])
            bingus = False
            break
        else:
            bingus = True 
    if bingus:
        print(-1)



    # print("Distâncias")
    # print(distancias)
    # print("Preços")
    # print(lista_precos)







        






        
