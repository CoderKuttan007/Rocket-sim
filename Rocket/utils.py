import pygame

def scale_img(img, factor):
    size = round(img.get_width() * factor), round(img.get_width() * factor)
    return pygame.transform.scale(img, size)
