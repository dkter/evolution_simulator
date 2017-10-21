import creature
import pyglet

window = pyglet.window.Window(
    width=800,
    height=650,
    caption="EVOLUTION SIMULATATRON 3000")

bob = creature.Creature(1, 1, 1, 1, 1, 1, 100, 100)

pyglet.gl.glClearColor(1, 1, 1, 1)


@window.event
def on_draw():
    window.clear()
    bob.draw()


def update(dt):
    pass


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
