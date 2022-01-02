import pygame
from mathFunct import *
from objects_level import *
import sys


def main():
    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    gameDisplay = pygame.display.set_mode((800, 600))
    gameDisplay.fill((0, 0, 0))

    object_level_1 = ObjectLevel(gameDisplay)
    planet_1 = Planet(
        {'x': 100, 'y': 200, 'mass': 800000000000, 'color': red}, "planetA")
    planet_2 = Planet({'x': 200, 'y': 600, 'mass': 100,
                       'color': green}, "planetB")
    planet_3 = Planet({'x': 200, 'y': 100, 'mass': 100,
                       'color': blue}, "planetC")
    the_sun = Planet({'x': 200, 'y': 100, 'mass': 1000000000,
                      'color': blue}, "sun")

    object_level_1.add_object(planet_1)
    object_level_1.add_object(planet_2)
    object_level_1.add_object(planet_3)
    object_level_1.add_object(the_sun)

    object_level_1.set_zoom_level(0.5)

    while (True):

        gameDisplay.fill((0, 0, 0))
        object_level_1.process_physics()
        object_level_1.render_objects()
        the_sun.x = 0
        the_sun.y = 0

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    object_level_1.set_zoom_level(
                        object_level_1.zoom_level * 1.50)
                if event.key == pygame.K_z:
                    object_level_1.set_zoom_level(
                        object_level_1.zoom_level * 0.50)

    sys.exit()


if __name__ == '__main__':
    main()
