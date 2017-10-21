import pyglet

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

creature = pyglet.resource.image("creature.png")
