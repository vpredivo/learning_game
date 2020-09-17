import random
import pygame
from pygame.locals import QUIT
import utils
import AI 

SCREEN_SIZE = 300
SURFACE = 10
SAMPLE_NUMBER = 10

COEF_A = random.random()*4
COEF_B = random.randint(0, 20)
SIDE = random.random()

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE + 120))


pygame.display.set_caption('Learning Game')

screen.fill((0, 0, 0))

#drawing split line from playing screen and buttons
for i in range(int(SCREEN_SIZE/5)):
    pygame.draw.rect(screen, (255, 200, 100), (i*10, SCREEN_SIZE+15, 5, 5))

pygame.display.update()


objectsRect = []
clickedObj = []
AMOUNT = 100

SolveButton = utils.button((0, 255, 0), 10, SCREEN_SIZE+25, 120, 50, 'Solve', estate = 0)
SolveButton.draw(screen, (0, 0, 0))
# SolveButtonEstate = 0

GuessButton = utils.button((100, 50, 100), 170, SCREEN_SIZE+25, 120, 50, 'Guess', estate = 0)
GuessButton.draw(screen, (0, 0, 0))
# GuessButtonEstate = 0

AIButton = utils.button((50, 50, 150), 10, SCREEN_SIZE+90, 280, 20, 'AI', estate = 0)
AIButton.draw(screen, (0, 0, 0))
# AIButtonEstate = 0

PointsTrueValue = []
PaintedPoints = []
GuessedPoints = []
x_pos = []
y_pos = []

for i in range(0, AMOUNT):
    x, y = utils.on_grid_random(SCREEN_SIZE = SCREEN_SIZE, SURFACE = SURFACE)
    objectsRect.append(pygame.draw.rect(screen, (255, 255, 255), (x, y, 10, 10)))
    x_pos.append(x)
    y_pos.append(y)

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


#
# GAME LOOP
#

while True:
    clock.tick(20)
    
    if AIButton.estate == 0 : #Human playing
        if SolveButton.estate == 0:
            if GuessButton.estate == 0:
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
                if pressed1 and GuessButton.estate == 1 and mouse_pos[1] < SCREEN_SIZE:
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
                    clickedObj = utils.points_reveal(clickedObj)
                    SolveButton.estate = 1


                elif GuessButton.isOver(mouse_pos):
                    GuessButton.changeEstate()

                elif AIButton.isOver(mouse_pos):
                    AIButton.changeEstate()

                else:
                    for i in range(len(objectsRect)):
                        if objectsRect[i].collidepoint(mouse_pos) and GuessButton.estate == 0:
                            clickedObj[i] = 1
            
            

    else: #AI playing
        Machine = AI.AI()
        if sum(clickedObj) == 0:
            rand = random.randint(0, AMOUNT-2)
            clickedObj[rand] = 1
            clickedObj[rand + 1] = 1
        elif sum(clickedObj) <= SAMPLE_NUMBER:
            rand = random.randint(0, AMOUNT-2)
            clickedObj[rand] = 1
            pygame.time.wait(1000)
        else:
            GuessedPoints = Machine.fit_predict(x_dim = x_pos, y_dim = y_pos, real_value = PointsTrueValue, known_data = clickedObj)
            print(GuessedPoints)
             
            print('ACABOU')
            AIButton.changeEstate()
    
    
    for i in range(len(objectsRect)):
                utils.color_point(objectsRect[i],clickedObj[i], COEF_A = COEF_A, COEF_B = COEF_B, SIDE = SIDE, screen = screen)            


    pygame.display.update()
