import pygame
import random
import sys
import time
from Graph import *
from pygame.locals import *

#Parameters for window size and mouse buttons
WIDTH = 1200
HEIGHT = 800
MOUSELEFT = 0
MOUSEMIDDLE = 1
MOUSERIGHT = 2

RADIUS = 10

#colors
BROWN = (255,64,64) #Node
COLDGREY = (128,138,135)
WHITE = (255,248,220) #Edge
FUCSIA = (238,18,137) #Selected node
BLUE = (30,144,255) #Selected edge
BLACK = (0,0,0)

def get_positions(vertices,amount):
    x = 950//amount
    y = 450//amount
    X = [i*x+15 for i in range(amount)]
    Y = [i*y+15 for i in range(amount)]

    positions = []
    for v in vertices:
        pos_x = random.choice(X)
        pos_y = random.choice(Y)
        positions.append((pos_x,pos_y))
        X.remove(pos_x)
        Y.remove(pos_y)
    return positions

def distance(x0, x1):
    return((x0[0]-x1[0])**2 +(x0[1]-x1[1])**2 )**0.5


class Visualizer:
    def __init__(self,graph):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.G = graph #grafo
        self.posiciones_nodos = get_positions(self.G.vertices(),len(self.G.vertices()))

        #Flags 
        self.selected_vertex = False
        self.moving_vertex = 0
        self.edge_line = False
        #self.drawing_line = 0

    def play(self):
        self.flag_= True
        while self.flag_:
            self.screen.fill(BLACK)
            self.graphics()
            pygame.display.update()
            self.Events()
        pygame.quit()
        sys.exit()
    
    def graphics(self):
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans Ms', 15)
        for nodo in self.G.vertices():
            self.drawing_vertex(nodo, self.posiciones_nodos[nodo])
        for edge in self.G.edges():
            v1,v2, w = edge[0],edge[1],edge[2]
            self.drawing_line(v1,v2)
            self.write_weight(v1,v2, w, True)

    def Events(self): #defining if quiting or clicking
        pygame.event.pump()
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.flag_ = False

            elif event.type == MOUSEBUTTONDOWN:
                button = mouse_buttons.index(True)
                self.click(button)
    
    def click(self, button): #This method is for deciding if clicked over a vertex, move vertex or create edge
        hovering, vertice = self.hover_vertex()
        self.d_line = False
        if (hovering==True and button==MOUSERIGHT) or self.d_line==True:
            self.d_line = True
            self.Create_edge(vertice)
        elif hovering==True and button == MOUSELEFT:
            self.Moving_vertex(vertice)
        return

    def hover_vertex(self):#This returns if a mouse is over a vertex and the vertex
        selected_vertex = False
        vertice = None
        self.mouse_position = pygame.mouse.get_pos()
        for v in self.G.vertices():
            distancia = distance(self.mouse_position, self.posiciones_nodos[v])
            if distancia<RADIUS:
                selected_vertex = True
                vertice = v
                return selected_vertex, vertice
            else:
                vertice = None
                selected_vertex = False
        return selected_vertex, vertice   

    def Create_edge(self,vertice): #This method calls for drawing an edge and input weight or erase current line
        position_vertice = self.posiciones_nodos[vertice]
        pygame.event.pump()
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        def in_area(v1,v2,radius=RADIUS):
            if (v1[0]<v2[0]-radius) or (v1[0]>v2[0]+radius):
                #limite por izquierda y derecha
                return False
            elif (v1[1]<v2[1]-radius) or (v1[1]>v2[1]+radius):
                #limite por arriba y abajo
                return False
            else:
                return True


        while self.d_line==True:
            self.drawing_line(position_vertice, mouse_pos, BLUE, True)
            hovering, vertice2 = self.hover_vertex()
            self.d_line = True
            print(mouse_buttons)
            while mouse_buttons[2] ==True:
                self.drawing_line(position_vertice, mouse_pos, BLUE, True)
                self.drawing_line(position_vertice, mouse_pos, BLACK, True)   
                continue
            if hovering==True and in_area(vertice,vertice2) ==False:
                self.drawing_line(position_vertice, mouse_pos, BLUE, True)
                self.d_line = False
                break
                #w = self.input_weight()
                #print(w)
                #self.G.add_edge(vertice,vertice2, w)
                #self.write_weight(vertice, vertice2, w, False)
                #self.G.add_edge(vertice,vertice2, w)
            #    print("line")

                
                #self.display_message("No vertex selected")
                #break
            #else:
            #    print("no")
                #continue
            #    break
        return

    def Moving_vertex(self,vertice): #This method cass for drawing a vertex
        while pygame.event.get() == pygame.MOUSEBUTTONDOWN:
            print("hi")
            self.drawing_vertex(vertice, pygame.mouse.get_pos(), True)
        self.drawing_vertex(vertice, pygame.mouse.get_pos())
        return
    
    def drawing_line(self,v1, v2, Color=WHITE, creating=False):
        if creating==True:
            pygame.draw.line(self.screen, 
                                color=Color, 
                                start_pos=v1, 
                                end_pos=v2, 
                                width=4)

        else:
            pygame.draw.line(self.screen, 
                                color=Color, 
                                start_pos=self.posiciones_nodos[v1], 
                                end_pos=self.posiciones_nodos[v2], 
                                width=4)

    def display_message(self,message):
        self.myfont.render_to(self.screen, (900,400), message, WHITE)
    
    def input_weight(self): #This method calls for getting keyboard press
        print("w")
        def get_key():
            while 1:
                pygame.event.pump()
                mouse_pos = pygame.mouse.get_pos()
                mouse_buttons = pygame.mouse.get_pressed()

                event = pygame.event.poll()
                if event.type == pygame.KEYDOWN: return event.key
                else: pass

        pygame.draw.rect(self.screen, (0,0,0), 
                                (self.screen.get_width()/2 -100,self.screen.get_height()/2 -10, 200, 20), 0)
        pygame.draw.rect(self.screen, (255,255,255),
                                (self.screen.get_width()/2 -102,self.screen.get_height()/2 -12, 204, 24), 0)
        self.screen.blit(self.myfont.render("Input weight:", 1, (255,255,255)),
                                (self.screen.get_width()/2 -100,self.screen.get_height()/2 - 10))
        pygame.display.flip()

        val  = ""
        while 1:
            key = get_key()
            if key == pygame.K_RETURN: break
            else:
                val += str(key)
        val = int(val)
        return val
    
    def write_weight(self, v1,v2, w, already_existing=True): #Gets the weight for two vertex and writes it
        index = self.G.abs_w.index(w)
        pos1 = self.posiciones_nodos[v1]
        pos2 = self.posiciones_nodos[v2]
        mid_x = pos1[0] + abs(pos1[0]-pos2[0])/2.0
        mid_y = pos1[1] + abs(pos1[1]-pos2[1])/2.0

        if already_existing == True:
            textsurface = self.myfont.render(str(w), False, (255,255,255))
            self.screen.blit(textsurface,(mid_x + 2, mid_y+ 2))
        else:
            textsurface = self.myfont.render(str(w), False, (255,255,255))
            self.screen.blit(textsurface,(mid_x + 2,mid_y + 2))

    def drawing_vertex(self, vertice, posicion, moving =False):
        if moving:
            self.posiciones_nodos[vertice] = posicion
            pygame.draw.circle(self.screen, color=WHITE, center=self.posiciones_nodos[vertice],radius=RADIUS)
        else:
            pygame.draw.circle(self.screen, color=BLUE, center=self.posiciones_nodos[vertice],radius=RADIUS)
    