from pyglet.sprite import Sprite
import pyglet


class Food(Sprite):
    def __init__(self, init_x, init_y):

        self.pos = (init_x, init_y)

        pyglet.resource.path = ["resources"]
        pyglet.resource.reindex()
        food = pyglet.resource.image("food.png")

        super().__init__(food, x=init_x, y=init_y)
