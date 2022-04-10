import pygame, random

class Rocket:
    def __init__(self, rocket, x, y):
        self.x = x 
        self.y = y
        self.rocket = rocket
        self.flames = []
        self.flame_life_time = 0.2

    def propell(self):
        self.y -= 2

    def circle_surf(self, radius, color):
        surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, color, (radius, radius), radius)
        return surf

    def propellant_particles(self, win):
        offset_x = self.rocket.get_width() // 2 - 3
        offset_y = self.rocket.get_height() // 2 + 35

        flame_x = self.x + offset_x
        flame_y = self.y + offset_y

        self.flames.append([[flame_x, flame_y], [0, 1], random.randint(5, 10)])

        for flame in self.flames:
            flame[0][0] += flame[1][0]
            flame[0][1] += flame[1][1]

            flame[2] -= self.flame_life_time
            pygame.draw.circle(win, (222, 186, 44), [int(flame[0][0]), int(flame[0][1])], int(flame[2]))

            radius = int(flame[2]) * 2
            win.blit(self.circle_surf(radius, (212, 99, 51)), (int(flame[0][0] - radius), int(flame[0][1]) - radius), special_flags=pygame.BLEND_RGBA_MAX)

            if flame[2] <= 0:
                self.flames.remove(flame)
    
    def show(self, win):
        win.blit(self.rocket, (self.x, self.y))