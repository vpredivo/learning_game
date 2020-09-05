import random
import pygame
from pygame.locals import QUIT
from numpy import ones,vstack
from numpy.linalg import lstsq
import utils

SCREEN_SIZE = 300
SURFACE = 10
SAMPLE_NUMBER = 3

COEF_A = 1 #random.randint(0, 2)
COEF_B = 0 #random.randint(0, 30)

def on_grid_random():
    """
    create random coordenates
    """
    x = random.randint(0, SCREEN_SIZE - SURFACE)
    y = random.randint(0, SCREEN_SIZE - SURFACE)
    return (x//10*10, y//10*10)



def color_point(rec):
    """
    create colorful point
    """
    if rec.left*COEF_A + COEF_B <= rec.top:
        r = 255
        g = 0
        b = 0
    else:
        r = 0
        g = 255
        b = 255
    return pygame.draw.rect(screen, (r, g, b), (rec.left, rec.top, 10, 10))

def rotate_90(pos):
    x = pos[0]*0 - pos[1]*1 
    y = pos[0]*1 + pos[1]*0
    return x,y

def draw_line(pos1, pos2):
    """
    draw guessing line
    """

    # x1,y1 = rotate_90(pos1)
    # x2,y2 = rotate_90(pos2)

    x1,y1 = pos1
    x2,y2 = pos2

    a = (y1-y2)/(x1-x2)
    b = y1 - x1*a
    # points = [pos1,pos2]
    # x_coords, y_coords = zip(*points)
    # A = vstack([x_coords,ones(len(x_coords))]).T
    # m, c = lstsq(A, y_coords)[0]
    print((x1,y1),(x2,y2))
    return pygame.draw.aaline(screen, (200, 0, 200), (0, b), (SCREEN_SIZE, SCREEN_SIZE*a + b))




pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE + 100))


pygame.display.set_caption('Learning Game')

screen.fill((0, 0, 0))

#drawing split line from playing screen and buttons
for i in range(int(SCREEN_SIZE/5)):
    pygame.draw.rect(screen, (255, 200, 100), (i*10 ,SCREEN_SIZE+10, 5, 5))

pygame.display.update()


objectsRect = []
clickedObj = []
AMOUNT = 100

for i in range(0, AMOUNT):
    x, y = on_grid_random()
    objectsRect.append(pygame.draw.rect(screen, (255, 255, 255), (x, y, 10, 10)))
    clickedObj.append(0)

GreenButton = utils.button((0,255,0), 10, SCREEN_SIZE+25, 100, 50, 'Solve')
GreenButton.draw(screen, (0,0,0))


pygame.display.update()


mouse_pos_line_count = 0
mouse_pos_line1 = 0
mouse_pos_line2 = 0

clock = pygame.time.Clock()
def redrawWindow():
    screen.fill((0,0,0))
    GreenButton.draw(screen, (0,0,0))

while True:
    clock.tick(20)
    # redrawWindow()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == QUIT:
            pygame.quit()
        
        elif event.type == pygame.MOUSEMOTION:
            if pressed1 and sum(clickedObj) == SAMPLE_NUMBER:
                last = (event.pos[0]-event.rel[0], event.pos[1]-event.rel[1])
                pygame.draw.line(screen, (100,100,0), last, event.pos, 10)
            if GreenButton.isOver(mouse_pos):
                GreenButton.color = [0,170,0]
            else :
                GreenButton.color = [0,255,0]


            

        
        
        else :
            for i in range(len(objectsRect)):
                if objectsRect[i].collidepoint(mouse_pos) and pressed1 and clickedObj[i] == 0:
                    color_point(objectsRect[i])
                    clickedObj[i] = 1
                    print('clicou') 
                elif clickedObj[i] > 0 :
                    color_point(objectsRect[i])
                # elif sum(clickedObj) < SAMPLE_NUMBER : 
                #     pygame.draw.rect(screen, (255, 255, 255), (objectsRect[i].left, objectsRect[i].top, 10, 10))
                # else :
                #     color_point(objectsRect[i])
    
    # for i in range(len(objectsRect)):
    #     if sum(clickedObj) + 1 == SAMPLE_NUMBER and ~objectsRect[i].collidepoint(mouse_pos):
    #         if pressed1 and mouse_pos_line_count == 0:
    #             mouse_pos_line1 = mouse_pos
    #             mouse_pos_line_count = mouse_pos_line_count + 1
                
    #         if pressed3 and mouse_pos_line_count == 1 :
    #             mouse_pos_line2 = mouse_pos

    #             draw_line(mouse_pos_line1,mouse_pos_line2)


    pygame.display.update()
