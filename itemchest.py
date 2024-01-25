import pygame as pg
from mouse import Mouse
from support import loadSprite
from timer import Timer

class ItemChest(pg.sprite.Sprite):
  def __init__(self,name,inventory,pos,group):
      super().__init__(group)
      spritePath = f"Sprites/Chests/"
      self.inventory = inventory
      self.image = loadSprite(f"{spritePath}{name}.png",(100,100)).convert_alpha()
      self.rect = self.image.get_rect(topleft=pos)
      self.hitbox = self.rect.inflate(0,0)

