from Graph import *
import random

def Prim(G):
    vertices = G.vertices()
    edges = G.edges()

    vertices_explorados = random.choice(vertices)
    aristas_por_explorar = edges[vertices_explorados[0]]

    Tree = Graph()

    return