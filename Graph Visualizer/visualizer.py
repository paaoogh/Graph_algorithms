import pygame
import random
import sys
from Graph import *
from pygame.locals import *

#FALTA AGREGAR COLORES EN TUPLAS

WIDTH = 1200
HEIGHT = 800
MOUSELEFT = 1
MOUSEMIDDLE = 2
MOUSERIGHT = 3

def get_middle(x,y):
    return x[0]+(abs(x[0]-y[0])/2), x[1]+(abs(x[1]-y[1])/2)


class Visualizer:
    def __init__(self, graph):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.G = graph #grafo
        self.posiciones_nodos = [(random.randrange(20,1000), random.randrange(20,500)) for v in self.G.vertices()]

        self.selected_vertex = False
        self.moving_vertex = 0
        self.edge_line = False
        self.drawing_line = 0

        print(self.G.vertices(), self.G.edges())

    def play(self):
        self.flag_= True
        while self.flag_:
            self.screen.fill((0, 0, 0))
            self.graphics()
            pygame.display.update()
            self.Events()
        pygame.quit()
        sys.exit()

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.flag_ = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.click(event.button) 

    def hovering_vertex(self, u):
        self.mouse_position = pygame.mouse.get_pos()
        for vert in self.G.vertices():
            dis = (self.posiciones_nodos[vert][0]-self.mouse_position[0])+(self.posiciones_nodos[vert][1]-self.mouse_position[1])**2
            if dis <30:
                self.selected_vertex = True
                return vert
        return self.selected_vertex 
        

    def click(self,button):
        #STILL WORKING ON THIS PART
        if button == MOUSELEFT and self.selected_vertex==False:
            self.mouse_position = pygame.mouse.get_pos()
            pygame.draw.circle(self.screen,color=(0,100,100),center=self.mouse_position, radius = 10)
            G.add_node()
            selected_vertex = False

        elif button == MOUSERIGHT or self.edge_line == True:
            pygame.draw.line(self.screen, color=(200,0,0), 
                                start_pos=self.posiciones_nodos[self.G.edges()[-1]],
                                end_pos=self.posiciones_nodos[self.G.edges()[-2]], width=4)
            G.add_vertex(self.G.edges()[-1], self.G.edges()[-2],random.random())
            edge_line=False


        #elif button == MOUSERIGHT: #select vertex for moving
        #    if self.edge_line != False and self.drawing_line != self.moving_vertex:
        #        self.G.add_edge(self.edge_line,self.moving_vertex)
        #        self.edge_line = True
        #    self.drawing_line = 1
        return

    def graphics(self):
        pygame.font.init() 
        myfont = pygame.font.SysFont('Comic Sans MS', 15)   
        #Draw line, add vertex
        for nodo in self.G.vertices():
            flag = self.hovering_vertex(nodo)
            if flag!=False:
                color = (0,0,255)
            else:
                color = (0,40,255)
            pygame.draw.circle(self.screen,color=color,center=self.posiciones_nodos[nodo],radius=10)

        for edge in self.G.edges(): #from a given graph
            pygame.draw.line(self.screen, color=(200,255,0), 
                                start_pos=self.posiciones_nodos[edge[0]], 
                                end_pos=self.posiciones_nodos[edge[1]],width=4)
            #FALTA ESCRIBIR LOS PESOS

        for weight in range(len(self.G.abs_w)):
            #Writing weights
            x,y = get_middle(self.posiciones_nodos[weight-1],self.posiciones_nodos[weight])
            textsurface = myfont.render(str(self.G.abs_w[weight]), False, (255, 255, 255))
            self.screen.blit(textsurface,(x,y))
            
        if self.drawing_line != 0: #me drawing it
            pygame.draw.line(self.screen, color=(200,155,10), start_pos=self.posiciones_nodos[self.drawing_line], 
                            end_pos=pygame.mouse.get_pos(),width=3)
            self.drawing_line = 0
