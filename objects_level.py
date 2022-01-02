from planet import *
import mathFunct
import pygame


class ObjectLevel:
    def __init__(self, screen):

        self.screen = screen
        self.objects = []
        self.zoom_level = 1

    def add_object(self, object_):
        if not (object_):
            return False

        self.objects.append(object_)

    def render_objects(self):
        for object_ in self.objects:
            object_.render_intern(self.screen, self.zoom_level)

    def update_objects(self):
        for object_ in self.objects:
            object_.update_intern()

    def process_physics(self):
        # for object_a in self.objects:
        #     for object_b in self.objects:
        #         if (object_a != object_b):

        #             acc_x, acc_y = mathFunct.accelleration(
        #                 object_a.x, object_b.x,
        #                 object_a.y, object_b.y, mathFunct.calculate_gravitational_accelleration(object_a.mass, mathFunct.distance(object_a.x, object_b.x, object_a.y, object_b.y)*2))
        #             object_b.speed_x += acc_x
        #             object_b.speed_y += acc_y

        #             print(mathFunct.calculate_gravitational_accelleration(
        #                 object_a.mass, mathFunct.distance(object_a.x, object_b.x, object_a.y, object_b.y)*2))

        #             object_b.x += object_b.speed_x
        #             object_b.y += object_b.speed_y
        print('---------------------------')

        for object_a in self.objects:

            object_a.x += object_a.speed_x
            object_a.y += object_a.speed_y
            # if (object_a.x > 1000 or object_a.x < -1000):
            #     object_a.x = 0
            # if (object_a.y > 1000 or object_a.y < -1000):
            #     object_a.y = 0

            for object_b in self.objects:
                print(object_a.name, object_b.name)
                print(mathFunct.distance(object_b.x,
                                         object_a.x,
                                         object_b.y,
                                         object_a.y))

                print(object_a.name, object_a.x, object_a.y)

                if (mathFunct.distance(object_a.x, object_b.x, object_a.y, object_b.y) == 0):
                    continue

                print(object_a.name, ' gravity ', mathFunct.calculate_gravitational_accelleration(
                    object_a.mass, mathFunct.distance(object_a.x, object_b.x, object_a.y, object_b.y)))

                acc_x, acc_y = mathFunct.accelleration(
                    object_a.x, object_b.x, object_a.y, object_b.y,
                    mathFunct.calculate_gravitational_accelleration(
                        object_a.mass, mathFunct.distance(object_a.x, object_b.x, object_a.y, object_b.y))
                    # object_a.mass
                )

                object_b.speed_x += acc_x
                object_b.speed_y += acc_y

    def set_zoom_level(self, new_zoom_level):
        self.zoom_level = new_zoom_level
