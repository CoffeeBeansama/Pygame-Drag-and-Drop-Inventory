import pygame as pg
from inventoryslot import InventorySlot
from support import drawBox

class ChestInventory:
    def __init__(self):
        self.screen = pg.display.get_surface()

        self.xPos,self.yPos = 10,20
        self.width,self.height = 680,280
    
    def handleRendering(self):
        background = drawBox(self.screen,
                             self.xPos,self.yPos,
                             self.width,self.height)
    
    def update(self):
        self.handleRendering()
