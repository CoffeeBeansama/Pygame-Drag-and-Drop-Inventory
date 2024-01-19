import pygame as pg
from inventoryslot import InventorySlot
from support import drawBox


class PlayerInventory:
    def __init__(self):
        self.screen = pg.display.get_surface()
        
        self.xPos,self.yPos = 10,315
        self.width,self.height = 680,100

    def handleRendering(self):        
        background = drawBox(self.screen,self.xPos,self.yPos,
                             self.width,self.height)

    def update(self):
        self.handleRendering()
