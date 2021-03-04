import pygame 
from pygame.locals import *
import sys,math

WIDTH = 640
HEIGHT = 480

class Node:
    def __init__(self,radius=0.5,select=False):
        self.radius=0.5
        self.select = select

    def crear(radius=1):
        position = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0,0,255), position, 10)

    def conectar(self):
        return


class Edge: #Aún por trabajar!! 
    #def __int__(self, A,B):
    #    self.B = (x2,y2)
    ##    self.A = (x1,y1) 

    def unir(A,B):
        pygame.draw.line(screen, (0,255,0), A,B, 1)
        return


def create_vertex(pos1, pos2,lista):
    for i in range(len(lista)-2):
        pos1 = lista[i]
        pose2 = lista[i+2]
        points = math.ceil(((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)**0.5)
        pygame.draw.line(screen,(0,255,0),pos1,pos2, 1)
    lista = []
    return lista
   

def main():
    nodos = 0
    nodes = {}
    sostener = False
    global lista
    lista = []
    while True:
        for event in pygame.event.get():
            pygame.display.update()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN and event.button==1: ## Crear nodo
                nodo = Node()
                nodo.crear()

                nodos += 1
                nodes[pygame.mouse.get_pos()] = []
                print(nodes)
            
            elif event.type == MOUSEBUTTONDOWN and event.button==3 and sostener==False: #Crear vértice 
                A = pygame.mouse.get_pos()
                lista.append(A)
                pygame.event.wait()
                sostener = True

                if event.type == MOUSEBUTTONDOWN and event.button==3 and sostener==True:
                    B = pygame.mouse.get_pos()
                    lista.append(B)
                    
                    create_vertex(A,B,lista)
                    sostener = False
                    pygame.display.flip()
                
                    if A in nodes.keys():
                        nodes[A].append(B)
                    elif A not in nodes.keys():
                        nodes[A] = [B]
                    
                    if B in nodes.keys():
                        nodes[B].append(A)
                    elif A not in nodes.keys():
                        nodes[B] = [A]

            elif event.type == pygame.KEYDOWN and event.key== pygame.K_RETURN:
                lista = []                   

 
    return 0
 
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((255, 255, 255))
    main()
