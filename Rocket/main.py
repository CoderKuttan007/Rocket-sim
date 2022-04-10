import pygame, sys

from rocket import Rocket
from utils import scale_img

# Basic setup
pygame.init
window_size = (800, 600)
running = True
clock = pygame.time.Clock()
FPS = 120
win = pygame.display.set_mode(window_size)
pygame.display.set_caption("Rocket go phoosh")

# loading images
rocket_img = scale_img(pygame.image.load('Assets/rocket.png').convert_alpha(), 1.5)

# Rocket
rocket = Rocket(rocket_img, window_size[0] // 2 - rocket_img.get_width() // 2, window_size[1])

while running:
    win.fill((10, 10, 10))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rocket.propellant_particles(win)
    rocket.show(win)
    rocket.propell()

    if rocket.y < -200:
        rocket.y = window_size[1]

    clock.tick(FPS)
    pygame.display.update()
