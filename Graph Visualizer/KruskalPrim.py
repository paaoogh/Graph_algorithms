from Graph import *
from visualizer import *
from random_graph import *
import random


def Prim(G):
    Vertex = G.vertices()
    Edges = G.edges()
    Vertex_visited = [random.choice(Vertex)]
    edges_to_visit = [list(Edges[Vertex_visited[0]])]
    Tree = Graph(Vertex[-1]+1)

    while edges_to_visit:
        #len(Tree.edges())<Vertex[-1]:
        edges_to_visit.sort(key=lambda x:x[2])
        s = edges_to_visit[0]
        edges_to_visit.remove(s)
        u,v,w = s[0],s[1],s[2]
        if v not in Vertex_visited:
            Tree.add_edge(u,v,w)
            Vertex_visited.append(v)
            if u not in Vertex_visited:
                neigh_u = list(G.get_neighbors(u))
                for i in neigh_u:
                    if i not in Vertex_visited:
                        edges_to_visit.append([u,i[0],i[1]]) 
    
    return Tree

class disjoint_sets:
    def __init__(self,n):
        self.parent = [None]*n

    def root(self,u):
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
    #for v in G.vertices():
    #    se = set(v)
    vertices = set(vertices)
    edges.sort(key=lambda x:x[2])

    for v,u,w in edges:
        if dis_sets.same_component(v,u):
            print(v, u, " already in the same component.")
        else:
            print("Joining: ", v, u)
            Tree.add_edge(v,u,w)
            A.append((v,u,w))
            dis_sets.juntar(v,u)

    #__________Just for curiosity___________
    weights = []
    for u in A:
        weights.append(u[-1])
    print("Sum: ", sum(weights))
    return Tree


if __name__ == "__main__":
    G = ErdosRenyi(7,1)
    MPS_kruskal = Kruskal(G)
    #print(MPS_kruskal)

    #MPS_prim = Prim(G)
    #print(MPS_prim)

    V = Visualizer(G)
    #K = Visualizer(MPS_kruskal)
    #P = Visualizer(MPS_prim)
    #K.play()
    V.play()
    #P.play()
