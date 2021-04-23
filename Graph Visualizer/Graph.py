class Graph():
    def __init__(self,num_vert):
        self.num_vert = num_vert
        self.num_edge = 0
        self.vecinos = [[] for i in range(num_vert)] #
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
            for v in self.get_neighbors(u):
                edge_.append((u,v))
        return edge_

    def add_node(self):
        self.vecinos.append([])
        self.num_ver += 1
        return

    def add_edge(self,u,v):
        self.vecinos[u].append(v)
        self.vecinos[v].append(u)
        self.num_edge += 1
        return


    


    