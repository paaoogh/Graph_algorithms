from grafica_bipartita import *
from apareamientos import *

G = Grafica_bipartita(3,4)
G.add_edge(0,0)
G.add_edge(0,1)
G.add_edge(1,0)
G.add_edge(1,2)
G.add_edge(2,2)
G.add_edge(2,3)

unmatched,match_x,match_y,sin_aumento = Aumento_(G)
G_final,tup = construir_bipartita(match_x,match_y,3,4)
print("Apareamiento final: ",set(tup))
print("Unmatched vertex final: ",unmatched)