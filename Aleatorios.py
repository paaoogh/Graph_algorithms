import random
import math
from Graph import *
from Kruskal import disjoint_sets
from interface import *

def generate_weights(n):
    return [random.random() for i in range(n)]

def ErdosRenyi(n,p,weights=None):
    G = Graph(n)
    if weights == None:
        weights = generate_weights(n)
    for v in range(n):
        for u in range(v):
            if random.uniform(0,1)<p:
                G.add_edge(u,v,weights[u])
    return G


def RandomGraphMEdges(n,m,weights=None):
    G = Graph(n) 
    if weights==None:
        weights= generate_weights(n)
    E = [(u,v) for v in range(n) for u in range(v)]
    chosen = random.sample(E,m)
    for i in chosen:
        G.add_edge(i[0],i[1],weights[chosen.index(i)])
    return G

def RandomTree(n):
    G = Graph(n)
    dis_sets = disjoint_sets(n)

    cantidad_edges = 0
    cantidad_minima = n-1 #esto asegura la definicion de arboles 

    while cantidad_edges != cantidad_minima:
        u = random.randint(0,n-1)
        v = random.randint(0,n-1)
        while v == u: #Asegurarnos que tomamos distintos nodos
            v = random.randint(0,n-1)

        if dis_sets.same_component(u,v)==False:
            weight = random.random()
            G.add_edge(u,v,weight)
            dis_sets.juntar(u,v)
            cantidad_edges += 1

    #print(dis_sets.parent)
    return G


def GrafoConexoAleatorio(mini,maxi):
    n = random.randint(mini,maxi)
    edges = random.randint(mini-1,maxi-1)
    while edges >=n:
        edges = random.randint(mini-1,maxi-1)
    return ErdosRenyi(n,0.5)

