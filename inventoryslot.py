import pygame as pg

class InventorySlot:
    def __init__(self,pos,data):
        
        self.pos = pos
        self.background = None
        self.itemData = data
        self.itemSprite = None

