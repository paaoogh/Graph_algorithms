from Graph import *
from interface import *
import random

class disjoint_sets:
    def __init__(self,n):
        self.parent = [None]*n
    
    def root(self, u):
        if self.parent[u] != None:
            self.parent[u] = self.root(self.parent[u])
            return self.root(self.parent[u])
        return u

    def juntar(self,u,v):
        self.root_u = self.root(u)
        self.root_v = self.root(v)
        self.parent[self.root_v] = u 

    def same_component(self,u,v):
        return self.root(u) == self.root(v)


def Kruskal(G):
    vertices = G.vertices()

    edges = G.edges()
    dis_sets = disjoint_sets(G.num_vert)
    A = []
    Tree = Graph(vertices[-1]+1)
    vertices = set(vertices)
    edges.sort(key=lambda x:x[2])

    grafo = Visualizer(G)
    grafo.play()

    for v,u,w in edges:
        if dis_sets.same_component(v,u):
            print(v,u, "already in the same component.")
        else:
            print("Joining: ", v, u)
            Tree.add_edge(v,u,w)
            A.append((v,u,w))
            dis_sets.juntar(v,u)
            grafo.drawing_line(v,u,BLUE)
    
    #_______________Just for curiosity______________________
    weights = []
    for u in A:
        weights.append(u[-1])
    print("Sum: ", sum(weights))
    return Tree
