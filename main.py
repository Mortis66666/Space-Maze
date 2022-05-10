import pygame

from utils.assets import BACKGROUND

WIDTH = BACKGROUND.get_width()
HEIGHT = BACKGROUND.get_height()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space maze")


def draw_background():
    win.blit(BACKGROUND, (0, 0))


def draw():
    draw_background()


    pygame.display.update()



def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()
        clock.tick(FPS)

    
    pygame.quit()

if __name__ == "__main__":
    main()