import pygame as pg
import sys
from playerinventory import PlayerInventory
from chestinventory import ChestInventory
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
        self.purchaseText = self.font.render("Inventory",True,white)

        self.timer = Timer(300)
        self.playerInventory = PlayerInventory()
        self.chestInventory = ChestInventory()

        self.renderInventory = False
    
    def handleInventoryButton(self):
        # Rendering
        self.inventoryButton = drawButton(self.screen,530,430,150,50,self.purchaseText)

        # Event

        if self.inventoryButton.collidepoint(Mouse.mousePosition()):
            if Mouse.pressingMouseButton() and not self.timer.activated:
                print("Open Inventory" if not self.renderInventory else "Close Inventory")
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
               self.playerInventory.update()
               self.chestInventory.update()

            pg.display.flip()

            self.clock.tick(60)



if __name__ == "__main__":
   game = Main()
   game.run()



