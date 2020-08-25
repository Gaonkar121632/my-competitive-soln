class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print("s",s)
            print("visited",visited)
            print("graph",self.graph)

            
            for i in self.graph[s]:
                if visited[i]==False:
                    visited[i]=True
                    queue.append(i)

g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)

g.bfs(0)



                    
