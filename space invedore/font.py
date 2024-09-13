import pygame
def font_render(font_family, font_size, text, tf, rgb):
    font = pygame.font.Font(font_family, font_size)
    font_render = font.render(text, tf, (rgb[0], rgb[1], rgb[2]))
    return font_render
