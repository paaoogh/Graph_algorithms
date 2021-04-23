import pygame
import random
from Graph import *
from pygame.locals import *

WIDTH = 800
HEIGHT = 600
MOUSELEFT = 1
MOUSEMIDDLE = 2
MOUSERIGHT = 3


class Visualizer:
    def __init__(self, graph):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.G = graph #grafo
        self.posiciones_nodos = [(random.random()*HEIGHT-10, random.random()*WIDTH-10) for v in self.G.vertices()]

        self.selected_vertex = False
        self.moving_vertex = 0
        self.edge_line = False
        self.drawing_line = 0

    def play(self):
        self.flag_= True
        while self.flag_:
            self.screen.fill((0, 0, 0))
            self.graphics()
            pygame.display.update()
            self.Events()
        
        self.pygame.quit()
        self.sys.exit()

    def Events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self.flag_ = False
                self.pygame.quit()
                self.sys.exit()
            elif event == pygame.MOUSEBUTTONDOWN:
                self.click(self.button) #Which click is it
            elif event == pygame.MOUSEBUTTONUP:
                self.un_click(self.button) #Which click is it

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
        if self.button == MOUSELEFT:
            self.selected_vertex = True

        elif self.button == MOUSERIGHT: #select vertex for moving
            if self.edge_line != False and self.drawing_line != self.moving_vertex:
                self.G.add_edge(self.edge_line,self.moving_vertex)
                self.edge_line = True
        return

    def graphics(self):
        #Draw line, add vertex
        for nodo in self.G.vertices():
            flag = self.hovering_vertex(nodo)
            if flag!=False:
                color = (0,0,255)
            else:
                color = (0,40,255)
            pygame.draw.circle(self.screen,color=color,center=self.posiciones_nodos[nodo],radius=10)
        for edge in self.G.edges(): #from a given graph
            pygame.draw.line(self.screen, color=(200,255,0), start_pos=self.posiciones_nodos[edge[0]], end_pos=self.posiciones_nodos[edge[1]],width=4)

        if self.drawing_line != 0: #me drawing it
            pygame.draw.line(self.screen, color=(200,155,10), start_pos=self.posiciones_nodos[self.drawing_line], 
                            end_pos=pygame.mouse.get_pos(),width=3)
