
import pygame
import random



class button():
    
    
    def __init__(self, color, x, y, width, height, text='', estate = 0):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.estate = estate

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

    def changeEstate(self):
        self.estate = abs(self.estate - 1)
        return

def on_grid_random(SCREEN_SIZE,SURFACE):
    """
    create random coordenates
    """
    x = random.randint(0, SCREEN_SIZE - SURFACE)
    y = random.randint(0, SCREEN_SIZE - SURFACE)
    return (x//10*10, y//10*10)



def color_point(rec, revealed, COEF_A, COEF_B, SIDE, screen):
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


def points_reveal(clickedObj):
    clickedObj = [1 for x in clickedObj]
    return clickedObj