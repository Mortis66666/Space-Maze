import pygame
import os

def load(img: str, ext: str=".png"):
    return pygame.image.load(
        os.path.join("Assets", img + ext)
    )

BACKGROUND = load("background")
GROUNDS = [load(f"tile{i}") for i in range(2)]