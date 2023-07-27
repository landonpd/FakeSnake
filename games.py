#imports that are used for games
import pygame
from pygame import *
from math import *

#defining colors
WHITE= (255, 255, 255)
BLACK=(0, 0, 0)
GREY=(128,128,128)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
YELLOW=(239,225,28)
PURPLE=(102,0,204)
ORANGE=(255,128,0)

#defining things that are needed for the game to be visable( ex. makes the screen dimensions)
init()
size = (900, 700)
screen = display.set_mode(size, RESIZABLE)
clock =time.Clock()

#creates a button that when clicked performs an action
def button(msg,x,y,w,h,col,font_col,action=None,*argv): 
    args=()
    pos_mouse = mouse.get_pos()
    click = mouse.get_pressed()
    text=draw_text(msg, 'Calibri', 25,font_col)
    txt_w=text[1]
    txt_h=text[2]
    draw.rect(screen, col,(x,y,w,h))
    if  x+w > pos_mouse[0] > x and y+h > pos_mouse[1] > y:
        if click[0]==1 and action!=None:
            ret=action(*argv)
            if ret!=None:
                return ret
    screen.blit(text[0], [int((w-txt_w)/2+x),int((h-txt_h)/2+y)])

#writes anything somewhere, simplyfies the process to only a few lines instead of like 10. Set a variable equal to draw_text, then scren.blit using the the first object in the variable    
def draw_text(msg, font, size,color):
    text_font= pygame.font.SysFont(font, size, True, False)
    text = text_font.render(msg,True,color)
    text_dim=[]
    text_dim.append(text)
    text_dim.append(text.get_rect().width)
    text_dim.append(text.get_rect().height)
    return text_dim

#quites the game, makes it one line instead of two and makes it easier to remember
def quitgame():
    pygame.quit()
    quit()

