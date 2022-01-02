import pygame
import random
import mathFunct
import costants

RED = (255, 0, 0)


class Planet:
    def __init__(self, props={}, name=''):
        defaults = {
            'x': 0,
            'y': 0,
            'mass': 100,
            'diam': costants.DEFAULT_PLANET_RADIUS*2,
            'speed_x': random.randint(costants.SPEED * -100, costants.SPEED * 100) / 100,
            'speed_y': random.randint(costants.SPEED * -100, costants.SPEED * 100) / 100,
            'color': [random.randint(128, 255), random.randint(
                128, 255), random.randint(128, 255)]
        }

        self.color = props['color'] if (
            'color' in props) else defaults['color']
        self.x = props['x'] if (
            'x' in props) else defaults['x']
        self.y = props['y'] if (
            'y' in props) else defaults['y']
        self.speed_x = props['speed_x'] if (
            'speed_x' in props) else defaults['speed_x']
        self.speed_y = props['speed_y'] if (
            'speed_y' in props) else defaults['speed_y']
        self.diameter = props['diam'] if (
            'diam' in props) else defaults['diam']
        self.mass = props['mass'] if (
            'mass' in props) else defaults['mass']
        self.name = name

    def update_intern(self):
        pass

    def render_intern(self, screen, zoom):
        if (self.x > 10000 or self.x < -10000):
            self.x = 0
        if (self.y > 10000 or self.y < -10000):
            self.y = 0

        pygame.draw.circle(screen, self.color,
                           (int((self.x * zoom) + (screen.get_width()) / 2),
                            int((self.y * zoom) + (screen.get_height()) / 2)),
                           int(self.diameter*zoom))
