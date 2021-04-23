import sys
import random
from Graph import *
from visualizer import *
    
if __name__ == "__main__":
    G = Graph(5)
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(1,4)
    G.add_edge(1,2)
    
    V = Visualizer(G)
    V.play()