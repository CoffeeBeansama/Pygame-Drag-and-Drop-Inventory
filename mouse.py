import pygame as pg

class Mouse(object):

    mousePos = None
    mousePressed = None
    pressingMouse = None

    @staticmethod
    def handleMouseUpdate():

        Mouse.mousePos = pg.mouse.get_pos()
        Mouse.mousePressed = pg.mouse.get_pressed()

        Mouse.pressingMouse = True if Mouse.mousePressed[0] else False

    
    def mousePosition():
        return Mouse.mousePos

    def pressingMouseButton():
        return Mouse.pressingMouse

