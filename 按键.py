import sys
import pygame
from settings import Settings

pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type:
            print(event.type)
    screen.fill(ai_settings.bg_color)
    pygame.display.flip()




