from Graph import *
from Kruskal import disjoint_sets
from interface import *
from Aleatorios import *

def connected_components(G):
    #Regresa una lista que marca de que componente es cada elemento
    #Regresa cantidad de componentes
    componentes = [-1]*G.num_vert 
    color = 0

    vertices = G.vertices()
    for v in vertices:
        if componentes[v] != -1:
            continue
        elif componentes[v] == -1:
            frontera = [v]
            while frontera:
                top = frontera.pop(0)
                if componentes[top] != -1:
                    continue
                elif componentes[top]== -1:
                    componentes[top] = color
                    vecinos_top = G.get_neighbors(top)

                    for u in vecinos_top:
                        if componentes[u[0]] == -1:
                            frontera.insert(0,u[0])

            color += 1
    return componentes,color

def is_connected(G):
    componentes,color = connected_components(G)
    if color ==0:
        return True
    else:
        return False

def is_tree(G):
    #definicion de arbol
    return (len(G.edges)) + 1 == G.num_vert and is_connected(G)

def get_parents(G,root):
    #Me dan el grafo y el nodo que es la raiz
    padres = list(range(G.num_vert))
    
    padres[root] = None
    frontera = [root]

    while frontera:
        p = frontera.pop(0)

        for u in G.get_neighbors(p):
            if padres[p] == u[0]:
                continue
            padres[u[0]] = p
            if padres[u[0]] == root:
                padres[root] = None
                break
            frontera.insert(0,u[0])
    return padres

G = RandomTree(10)
V = Visualizer(G)
componentes,color = connected_components(G)

print(connected_components(G))

V.play()