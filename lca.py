from Graph import *
from Aleatorios import *
from Conexidad import *

def LCAnaive(G,root, u,v):
    padres = get_parents(G,root)
    u_ancestors = [u]
    while padres[u] != None:
        u_ancestors.append(padres[u])
        u = padres[u]
    u_ancestors = set(u_ancestors)
    if v in u_ancestors:
        return v
    while padres[v]!= None:
        v = padres[v]
        if v in u_ancestors:
            return v
    return


