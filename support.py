import pygame as pg
from settings import white,black



def drawButton(surface,xPos, yPos, width, height, text):    
    # Background
    pg.draw.rect(surface, white, (xPos, yPos, width, height))
    
    # Button
    button = pg.draw.rect(surface, black, (xPos + 5, yPos + 5, width - 10, height - 10))
    
    # Text
    surface.blit(text, (xPos + 18, yPos + 10))

    return button

def drawBox(surface,xPos, yPos, width, height):    
    # Background
    pg.draw.rect(surface, white, (xPos, yPos, width, height))
    
    # Box
    box = pg.draw.rect(surface, black, (xPos + 5, yPos + 5, width - 10, height - 10))

    return box
