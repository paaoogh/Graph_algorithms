import sys
import random
from Graph import *
from interface import *

if __name__=='__main__':
    G = Graph(5)
    G.add_edge(0,1,4)
    G.add_edge(0,2,5)
    G.add_edge(1,4,6)
    G.add_edge(1,2,7)
    G.add_edge(1,3,9)

    V = Visualizer(G)
    V.play()