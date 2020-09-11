import random
import pygame
from pygame.locals import QUIT
import utils
import numpy as np

SCREEN_SIZE = 300
SURFACE = 10
SAMPLE_NUMBER = 4

COEF_A = random.random()*4
COEF_B = random.randint(0, 20)
SIDE = random.random()

def on_grid_random():
    """
    create random coordenates
    """
    x = random.randint(0, SCREEN_SIZE - SURFACE)
    y = random.randint(0, SCREEN_SIZE - SURFACE)
    return (x//10*10, y//10*10)



def color_point(rec, revealed):
    """
    create colorful point
    """
    if SIDE < 0.5:
        if revealed == 1:
            if rec.left*COEF_A + COEF_B <= rec.top:
                r = 255
                g = 0
                b = 0
            else:
                r = 0
                g = 255
                b = 255
            return pygame.draw.rect(screen, (r, g, b), (rec.left, rec.top, 10, 10))
        else:
            return pygame.draw.rect(screen, (255, 255, 255), (rec.left, rec.top, 10, 10))
    else:
        if revealed == 1:
            if rec.left*COEF_A + COEF_B >= rec.top:
                r = 255
                g = 0
                b = 0
            else:
                r = 0
                g = 255
                b = 255
            return pygame.draw.rect(screen, (r, g, b), (rec.left, rec.top, 10, 10))
        else:
            return pygame.draw.rect(screen, (255, 255, 255), (rec.left, rec.top, 10, 10))


def points_reveal():
    global clickedObj
    clickedObj = [1 for x in clickedObj]
    return clickedObj


pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE + 100))


pygame.display.set_caption('Learning Game')

screen.fill((0, 0, 0))

#drawing split line from playing screen and buttons
for i in range(int(SCREEN_SIZE/5)):
    pygame.draw.rect(screen, (255, 200, 100), (i*10 ,SCREEN_SIZE+15, 5, 5))

pygame.display.update()


objectsRect = []
clickedObj = []
AMOUNT = 100

SolveButton = utils.button((0,255,0), 10, SCREEN_SIZE+25, 120, 50, 'Solve')
SolveButton.draw(screen, (0,0,0))
SolveButtonEstate = 0

GuessButton = utils.button((100,50,100), 170, SCREEN_SIZE+25, 120, 50, 'Guess')
GuessButton.draw(screen, (0,0,0))
GuessButtonEstate = 0

PointsTrueValue = []
PaintedPoints = []
GuessedPoints = []

for i in range(0, AMOUNT):
    x, y = on_grid_random()
    objectsRect.append(pygame.draw.rect(screen, (255, 255, 255), (x, y, 10, 10)))
    
    if SIDE < 0.5:
        if x*COEF_A + COEF_B <= y:
            PointsTrueValue.append(1)
        else:
            PointsTrueValue.append(0)
    else:
        if x*COEF_A + COEF_B >= y:
            PointsTrueValue.append(1)
        else:
            PointsTrueValue.append(0)
    clickedObj.append(0)
    GuessedPoints.append(0)



pygame.display.update()


mouse_pos_line_count = 0
mouse_pos_line1 = 0
mouse_pos_line2 = 0

clock = pygame.time.Clock()
def redrawWindow():
    screen.fill((0,0,0))
    SolveButton.draw(screen, (0,0,0))

while True:
    clock.tick(20)
    
    if SolveButtonEstate == 0:
        if GuessButtonEstate == 0:
            GuessButton.color = [100,50,100]
            GuessButton.draw(screen, (0,0,0))
        else:
            GuessButton.color = [200,100,200]
            GuessButton.draw(screen, (0,0,0))
    else:
        for i in range(len(objectsRect)):
            for j in range(len(PaintedPoints)):
                    if objectsRect[i].collidepoint(PaintedPoints[j]):
                        GuessedPoints[i] = 1
        
        score = len([i for i, j in zip(GuessedPoints, PointsTrueValue) if i == j]) / len(GuessedPoints)
        
        ScoreBanner = utils.button((255,255,235), 10, SCREEN_SIZE+25, 280, 50, 'Acc {}'.format(score))
        ScoreBanner.draw(screen, (0,0,0))


    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == QUIT:
            pygame.quit()
        

        elif event.type == pygame.MOUSEMOTION:
            if pressed1 and GuessButtonEstate == 1 and mouse_pos[1] < SCREEN_SIZE:
                last = (event.pos[0]-event.rel[0], event.pos[1]-event.rel[1])
                PaintedPoints.append((last[0],last[1]))
                PaintedPoints.append((last[0]+10,last[1]+10))
                PaintedPoints.append((last[0]+10,last[1]-10))
                PaintedPoints.append((last[0]-10,last[1]+10))
                PaintedPoints.append((last[0]-10,last[1]-10))

                pygame.draw.line(screen, (170,0,10), last, event.pos, 30)

                
        

        elif pressed1:
            if SolveButton.isOver(mouse_pos):
                SolveButton.color = [0,120,0]
                SolveButton.draw(screen, (0,0,0))
                clickedObj = points_reveal()
                SolveButtonEstate = 1


            elif GuessButton.isOver(mouse_pos):
                GuessButtonEstate = abs(GuessButtonEstate - 1)
                
            else:
                for i in range(len(objectsRect)):
                    if objectsRect[i].collidepoint(mouse_pos) and GuessButtonEstate == 0:
                        clickedObj[i] = 1
        
        for i in range(len(objectsRect)):
            color_point(objectsRect[i],clickedObj[i])

        
                        


    pygame.display.update()
