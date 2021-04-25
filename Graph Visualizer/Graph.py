class Graph():
    def __init__(self,num_vert):
        self.num_vert = num_vert
        self.num_edge = 0
        self.vecinos = [[] for i in range(num_vert)] 
        self.weights = [[] for i in range(num_vert)]
        self.abs_w = []
        return

    def vertices(self):
        #list of vertex
        return range(self.num_vert)

    def get_neighbors(self,u):
        #get neighbors of u
        return self.vecinos[u]

    def edges(self):
        #list of all edges
        edge_ = []
        for u in self.vertices():
            #pesos = self.get_weights(u)
            for v,w in self.get_neighbors(u):
                edge_.append((u,v,w))
                self.num_edge += 1
        return edge_

    def add_node(self):
        self.vecinos.append([])
        self.num_ver += 1
        return

    def add_edge(self,u,v,w):
        self.vecinos[u].append((v,w))
        self.vecinos[v].append((u,w))
        self.weights[u].append(w)
        self.weights[v].append(w)
        self.abs_w.append(w)
        self.num_edge += 1
        return

    def get_weights(self,u):
        return self.weights[u]


    def get_num_edges(self):
        return self.num_edge
    
