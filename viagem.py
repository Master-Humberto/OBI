
vnm = input().split()
v = int(vnm[0])
n = int(vnm[1])
m = int(vnm[2])
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
trajeto = input().split()
inicial = int(trajeto[0]) - 1
final = int(trajeto[1]) - 1
## LINE BREAKER Construtor do problema
precos = []
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

    precos.append(changus)
    changus = []
#print(grafao)
# Construtor do grafao

for i in range(0, len(grafo)):
   precos[grafo[i][0]-1][grafo[i][1]-1] = grafo[i][3]

for i in range(0,len(grafo)):
    grafao[grafo[i][0]-1][grafo[i][1]-1] = grafo[i][2]

print(grafao)
print(precos)

#### LINE BREAKER Construtor do Grafo
run = True
class ShortestPathAnd2ndShortestDijkstras:
    NO_PARENT = -1	
    path = []; #nodes in the shortest path
    allDists = set(); #list of shortest distance
    allPists = []; # lista de precos
    #use Dijkstra’s Shortest Path Algorithm, O(n^2) Space O(n)
    def shortestPath(self, adjacencyMatrix,matriz_precos,  src, dest, run) : 
        n = len(adjacencyMatrix[0]) 
        preco = 0
        shortest = {}
        visited = {}
        parents = {}
        for v in range(0, n, 1)  :
            shortest[v] =  1e10 
            visited[v] = False
        shortest[src] = 0; 
        parents[src] = self.NO_PARENT; 
        for i in range(1, n, 1) : 
            pre = -1; 
            min =  1e10; 
            for v in range(0, n, 1) : 
                if visited[v]==False and shortest[v] < min : 
                    pre = v; 
                    min = shortest[v]; 
            if pre == -1:
                run = False
                return run
            visited[pre] = True; 
            for v in range(0, n, 1)  : 
                dist = adjacencyMatrix[pre][v];                  
                if dist > 0 and ((min + dist) < shortest[v]) :   
                    parents[v] = pre
                    shortest[v] = min + dist 
                    preco += adjacencyMatrix[pre][v] 
        try:
            self.allDists.add(shortest[dest])
            self.addPath(dest, parents); 
            self.allPists.append()
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
    def find2ndShortest(self, adjacencyMatrix, src, dest, run) : 
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
            self.shortestPath(adjacencyMatrix, src, dest, run)

myobj = ShortestPathAnd2ndShortestDijkstras()

i = 0
run = True
caminhos = []
distancias = []
while run : 
    if i == 0: 
        myobj.shortestPath(grafao, inicial, final, run)
    else:
        myobj.find2ndShortest(grafao,inicial,final, run)

    try:
        distancias.append(list(myobj.allDists)[i])
    except IndexError:
        run = False
    i += 1




        




 
    
        
