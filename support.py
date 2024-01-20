import pygame as pg
import os
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
    
    box = pg.draw.rect(surface, black, (xPos + 5, yPos + 5, width - 10, height - 10))

    return box


def getImageNamesInFolder(path):
    """
    Gets all image in specified a folder and return it as list-
    without its file extension

    Parameters:
        - path (string): Folder containing all sprites needed
    """

    image_names = []
    for filename in os.listdir(path):
        if filename.lower().endswith(".png"):
            image_names.append(os.path.splitext(filename)[0])
    return image_names

def loadSprite(imagePath, scale):
    newImage = pg.transform.scale(pg.image.load(imagePath),scale)
    return newImage
