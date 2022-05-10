from abc import abstractmethod, abstractproperty

import pygame


class BaseSprite:
    def __init__(self, win: pygame.Surface, x: int, y: int, selectable: bool=True):
        self.win = win
        self.x = x
        self.y = y

        self.selectable = selectable
        self.selected = False


    @abstractproperty
    @property
    def image(self):
        pass


    def draw(self):
        self.win.blit(self.image, (self.x * 64, self.y * 64))

    def select(self):
        if self.selectable:
            self.selected = False
            return self
        return None

    @abstractmethod
    def handle(self):
        pass
