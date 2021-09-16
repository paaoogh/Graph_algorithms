from Graph import *

class Grafica_bipartita():
    def __init__(self,num_vertx,num_verty):
        self.num_vertx = num_vertx
        self.num_verty = num_verty
        self.vertex = num_vertx+num_verty

        self.num_edge = 0
        self.vecinos_x = [[] for i in range(num_verty)]
        self.vecinos_y = [[] for i in range(num_vertx)]
        self.weights = [[] for i in range(self.vertex)]
        self.abs_w = []
    
    def vertices(self,x=None,y=None):
        #list of vertex/nodes
        if x==None:
            #asking for y list
            return range(self.num_verty)
        elif y==None:
            #asking for x list:
            return range(self.num_vertx)

    def get_neighbors(self,u,x=None,y=None):
        #get neighbors of u
        if x==None:
            #u is in y
            return self.vecinos_y[u]
        elif y==None:
            #u is in x
            return self.vecinos_x[u]
    
    def edges(self,x=None,y=None):
        #list of all edges
        if x==None:
            #Getting edges on y
            edge_ = []
            for u in self.vertices(y=True):
                for v,w in self.get_neighbors(u,y=True):
                    edge_.append((u,v,w))
                    self.num_edge += 1
            return edge_
        if y==None:
            #Getting edges on x
            edge_ = []
            for u in self.vertices(x=True):
                for v,w in self.get_neighbors(u,x=True):
                    edge_.append((u,v,w))
                    self.num_edge += 1
            return edge_
    
    def add_node(self,x=None,y=None):
        if x==None:
            #Adding node to y
            self.vecinos_y.append([])
            self.num_verty += 1
        elif y == None:
            #adding node to x
            self.vecinos_x.append([])
            self.num_vertx += 1

    def add_edge(self,u,v,w=1):
        #U pertenece a x, v pertenece a y
        self.vecinos_y[u].append((v,w))
        self.vecinos_x[v].append((u,w))
        self.weights[u].append(w)
        self.weights[v].append(w)
        self.abs_w.append(w)
        self.num_edge += 1

    def get_num_vert(self):
        return self.vertex


