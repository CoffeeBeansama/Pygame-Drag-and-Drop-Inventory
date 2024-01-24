import pygame as pg
import sys
from inventory import Inventory
from mouse import Mouse
from settings import fontpath,white
from timer import Timer
from support import drawButton

class Main:
    def __init__(self):
        pg.init()
        pg.font.init()

        width, height = 700, 500
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("InventoryDragAndDrop")
        
        self.clock = pg.time.Clock()

        self.font = pg.font.Font(fontpath,26)
        self.openText = self.font.render(" Open Inventory",True,white)
        self.closeText = self.font.render(" Close Inventory",True,white) 
        self.timer = Timer(300)
        self.inventory = Inventory()

        self.renderInventory = False
    
    def handleInventoryButton(self):
        # Rendering
        width = 245 if not self.renderInventory else 255
        text = self.openText if not self.renderInventory else self.closeText
        self.inventoryButton = drawButton(self.screen,220,430,width,50,text)

        # Event
        if self.inventoryButton.collidepoint(Mouse.mousePosition()):
            if Mouse.pressingMouseButton() and not self.timer.activated:
                self.renderInventory = True if not self.renderInventory else False
                self.timer.activate()


    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                   pg.quit()
                   sys.exit()
                   break
            
            self.screen.fill("black")
            self.timer.update()
            Mouse.handleMouseUpdate()
            
            self.handleInventoryButton()

            if self.renderInventory:
               self.inventory.update()

            pg.display.flip()

            self.clock.tick(60)



if __name__ == "__main__":
   game = Main()
   game.run()



