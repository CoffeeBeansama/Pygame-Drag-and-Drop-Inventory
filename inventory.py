import pygame as pg
import os
from support import drawBox,loadSprite,getImageNamesInFolder
from settings import spritepath
from timer import Timer
from mouse import Mouse


class InventorySlot:
    def __init__(self,pos,data):        
        self.pos = pos
        self.background = None
        self.itemData = data
        self.itemSprite = None

class Inventory:
    def __init__(self):
        self.screen = pg.display.get_surface()
       
        self.slotSize = 70
        self.slotXOffset = 83

        self.initializePrimaryInventory()
        self.initializeSecondaryInventory()
        
        self.mouseObjectSprite = None
        
        self.slotToSwap = None

        self.timer = Timer(300)

    def initializePrimaryInventory(self):

        # Slots
        self.P_xPos,self.P_yPos = 10,315
        self.P_width,self.P_height = 680,100
        
        self.P_itemSlots = []
        self.P_maxSlots = 8

        self.P_slotXStart = 25
        yPos = 330

        # Default Items
        self.items = getImageNamesInFolder(spritepath)  

        # Slots
        for index in range(self.P_maxSlots):
            xPos = self.P_slotXStart + (index * self.slotXOffset)
            newSlot = InventorySlot((xPos,yPos),self.items[index])
            self.P_itemSlots.append(newSlot)
                
        # Sprites
        self.imageSprites = {}
        spriteSize = (62,62)
        for item in self.items:
            self.imageSprites[item] = loadSprite(f"{spritepath}{item}.png",spriteSize)


    def initializeSecondaryInventory(self):
        self.S_xPos,self.S_yPos = 10,20
        self.S_width,self.S_height = 680,280

        self.S_itemSlots = []
        self.S_maxSlots = 32

        self.S_slotXStart = 25

        rows,columns = 3,8
        yPos = 40

        for i in range(rows):
            for j in range(columns):
                xPos = self.S_slotXStart + (j * self.slotXOffset)
                self.S_itemSlots.append(InventorySlot((xPos,yPos),None))
            yPos += 85


    def handleRendering(self):         
        # Primary Inventory
        P_background = drawBox(self.screen,self.P_xPos,self.P_yPos,
                             self.P_width,self.P_height)

        for slot in self.P_itemSlots:
            slot.background = drawBox(self.screen,slot.pos[0],slot.pos[1],self.slotSize,self.slotSize)
            if slot.itemData:
               slot.itemSprite = self.screen.blit(self.imageSprites[slot.itemData],(slot.pos[0]+3,slot.pos[1]+3))


        # Secondary Inventory  
        S_background = drawBox(self.screen,self.S_xPos,self.S_yPos,
                             self.S_width,self.S_height)

        for slot in self.S_itemSlots:
            slot.background = drawBox(self.screen,slot.pos[0],slot.pos[1],self.slotSize,self.slotSize)
            if slot.itemData:
               slot.itemSprite = self.screen.blit(self.imageSprites[slot.itemData],(slot.pos[0]+3,slot.pos[1]+3))
        

    def canHoldItem(self):
        if Mouse.pressingMouseButton() and not self.timer.activated:
           if self.slotToSwap is None:
              return True
        return False
    
    def mouseObject(self,sprite):        
        return self.screen.blit(sprite,(Mouse.mousePosition()[0]-20,Mouse.mousePosition()[1]-20))

    def onMouseRelease(self):
        if self.slotToSwap:
           for slot in self.P_itemSlots + self.S_itemSlots:
               if slot.background.collidepoint(Mouse.mousePosition()):
                  self.slotToSwap.itemData,slot.itemData = slot.itemData,self.slotToSwap.itemData
           self.mouseObjectSprite = None
           self.slotToSwap = None

    def handleMouseEvent(self):
        for slot in self.P_itemSlots + self.S_itemSlots:
            if slot.background:
                if slot.background.collidepoint(Mouse.mousePosition()):
                    if self.canHoldItem():
                       self.mouseObjectSprite = self.imageSprites[slot.itemData] if slot.itemData is not None else None
                       self.slotToSwap = slot
                       self.timer.activate()

        # Mouse Object
        if Mouse.pressingMouseButton() and self.mouseObjectSprite:
           self.mouseObject(self.mouseObjectSprite)
        else:
           self.onMouseRelease()
        
        
    def update(self):
        self.timer.update()
        self.handleRendering()
        self.handleMouseEvent()
