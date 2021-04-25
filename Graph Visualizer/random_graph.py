from Graph import *
from KruskalPrim import * 
from visualizer import *
import random

def generate_weights(n):
    return [random.random() for i in range(n)]

def ErdosRenyi(n,p,weights=None):
    G = Graph(n)
    if weights ==None:
        weights = generate_weights(n)
    for v in range(n):
        for u in range(v):
            if random.random() < p:
                G.add_edge(u,v,weights[u])
    return G

def ErdosRandom(n,m,weights=None):
    G = Graph(n)
    if weights ==None:
        weights = generate_weights(n)
    E = [(u,v) for v in range(n) for u in range(v)]
    chosen = random.sample(E,m)
    for i in chosen:
        G.add_edge(i[0],i[1],weights[chosen.index(i)])
    return G 


def GrafoConexoAleatorio(n,e):
    #nodes and edges
    if e > n-1 or e<n-1:
        raise Exception("DEFINITION CORRUPTED: |V|-1 edges")
        return
    if n==1: 
        return G(1)    
    return

def RandomTree():

    return

def RandomBinaryTree():
    return

#________________________________UNIT TESTS____________
if __name__ == "__main__":
    print("Erdos Renyi con n y p:")
    ER = ErdosRenyi(5,1)
    print("Using 5 nodes, probability 1: ",ER.vertices, ER.edges)
    V = Visualizer(ER)

    print("Erdos Random con n y m:")
    Er_ran = ErdosRandom(5,4)
    M = Visualizer(Er_ran)

    V.play()
    M.play()


#_________________________ Conexidad________________
def connected_components():
    ver = G.num_vert
    componentes = [-1]* ver
    color = 0

    for v in G.vertices():
        if componentes[-1] != -1:
            continue
        
        frontera = []
        frontera.append(v)
        while frontera:
            top = frontera.pop(0)

            if componentes[top] != -1:
                continue
            
            componentes[p] = color

            for u in G.get_neighbors(top):
                if componentes[u] == -1:
                    frontera.append(u)
        color += 1
    return componentes,color

def is_connected(G):
    componentes,color = connected_components(G)
    if color ==0:
        return True
    else:
        return False


def is_tree(G):
    return (len(Graph(G).edges)) + 1 == Graph(G).num_vert and is_connected(G)


def find_parents(G,r):

    return



#_______________________________________LCA_______________________
def LCA(T,r,v,u):

    return