from Graph import *
from grafica_bipartita import *

def get_neig(x,G):
    #ESto es porque los vecinos vienen con pesos 
    ne = G.get_neighbors(x,x=True)
    vecinos = []
    for i in ne:
        vecinos.append(i[0])
    return vecinos

def Apareamiento_(G):
    n = G.get_num_vert()
    unmatched_X = []
    match_x = [None]*n
    match_y = [None]*n
    for x in G.vertices(x=True):
        vecinos = get_neig(x,G)
        for y in vecinos:
            if match_y[y]==None:
                match_x[x] = y
                match_y[y] = x
                break
        if match_x[x] == None:
            unmatched_X.append(x)
    return unmatched_X,match_x,match_y

def aplicar_camino_aumento(y, padres,unmatched_X,matched_x,matched_y):
    x = padres[y]
    while y!=None:
        y_ahora = unmatched_X[x]
        matched_y[y] = x
        matched_x[x] = y
        y = y_ahora
        x = padres[y]
        if x==None:
            return False
    return matched_x,matched_y

def EncontrarCaminoAumento(G,x,unmatched_X,match_x,match_y):
    #Aplicar frontera con BFS
    n = G.get_num_vert()
    padres = [None]*n
    frontera = [x]
    camino_x = []
    camino_y = []
    while frontera:
        x_ahora = frontera.pop(0)
        vecinos = get_neig(x_ahora,G)
        for y in vecinos:
            if padres[y] == None:
                padres[y] = x_ahora
                x_nuevo = match_y[y]
                if x_nuevo == None:
                    cx,cy = aplicar_camino_aumento(y,padres,unmatched_X,match_x,match_y)
                    camino_x.append(cx)
                    camino_y.append(cy)
                    if unmatched_X[x]==None:
                        return camino_x,camino_y
                    return camino_x,camino_y
            else:
                continue
    return camino_x,camino_y

def Aumento_(G):
    unmatched_X,match_x,match_y = Apareamiento_(G)
    print(unmatched_X,match_x,match_y)
    control = 0
    sin_aumento = 0
    while control!=len(unmatched_X):
        cx,cy = EncontrarCaminoAumento(G,unmatched_X[control],unmatched_X,match_x,match_y)
        if len(cx)==0 and len(cy)==0:
            control += 1
            sin_aumento += 1
        else:
            control = unmatched_X.pop(-1)
            sin_aumento = 0
    return unmatched_X,match_x,match_y,sin_aumento


def construir_bipartita(match_x,match_y,x,y):
    G = Grafica_bipartita(x,y)
    tup = []
    for iter in range(len(match_x)):
        if match_x[iter]!=None:
            G.add_edge(iter,match_x[iter])
            tup.append((iter,match_x[iter]))
        if match_y[iter]!=None:
            G.add_edge(match_y[iter],iter)
            tup.append((match_y[iter],iter))
    return G,tup