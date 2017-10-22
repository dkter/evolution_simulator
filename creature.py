from pyglet.sprite import Sprite
import pyglet
from dna_parser import parse_dna, distance
import dna_parser
import random
from config import window_width, window_height
import food
import mutation

creatures = []


class Creature(Sprite):
    signal = 0
    attacking = False
    cool = False

    def __init__(self, mutability_chance: int, creature_number: int,
                 max_health: int, speed: int, dna: str, init_x: int,
                 init_y: int):
        self.mutability_chance = mutability_chance
        self.creature_number = creature_number
        self.max_health = int((max_health / 100) * 50)
        self.relative_max_health = max_health
        self.speed = int((speed / 100) * 10)
        self.relative_speed = speed
        self.dna = dna

        self.health = self.max_health

        self.pos = (init_x, init_y)

        pyglet.resource.path = ["resources"]
        pyglet.resource.reindex()
        creature = pyglet.resource.image("creature.png")

        super().__init__(creature, x=init_x, y=init_y)

        self.label = pyglet.text.Label(str(self.health),
                  font_name='Times New Roman',
                  font_size=16,
                  x=self.x, y=self.y,
                  anchor_x='center', anchor_y='center')

    def say_hi(self):
        print("hi")

    def do_stuff(self, other_creatures, foods):
        global creatures

        if self.cool: self.say_hi()

        # initialize
        nearest = dna_parser.nearest(self, other_creatures)
        nearest_food = dna_parser.nearest(self, foods)
        self.votes = {
            "up": 0,
            "left": 0,
            "right": 0,
            "down": 0
        }

        # parse the dna
        try:
            exec(parse_dna(self.dna, other_creatures))
        except:
            # Syntax errors are terminal diseases.
            # Kill the creature to put it out of its misery
            creatures.remove(self)
            #del(self)
            #return
            pass

        # don't fall off the edge
        while True:
            mv = max(self.votes.values())
            direction = random.choice(
                [k for (k, v) in self.votes.items() if v == mv])

            if ((direction == "up" and self.y + self.speed >= window_height-16) or
                (direction == "down" and self.y - self.speed <= 16) or
                (direction == "left" and self.x - self.speed <= 16) or
                (direction == "right" and self.x + self.speed >= window_width-16)):
                del self.votes[direction]
            else:
                break

        if self.cool: print("direction:", direction)
        if self.cool: print("speed:", self.speed)

        # move
        if direction == "up":
            if self.cool: print("going up")
            self.y += self.speed
        elif direction == "down":
            self.y -= self.speed
        elif direction == "right":
            self.x += self.speed
        elif direction == "left":
            self.x -= self.speed

        # eat food
        if (nearest_food.x - 24 < self.x < nearest_food.x + 24 and
            nearest_food.y - 24 < self.y < nearest_food.y + 24):
            del foods[foods.index(nearest_food)]
            foods.append(food.Food(
                random.randint(0, window_width),
                random.randint(0, window_height)))
            if self.health < self.max_health:
                self.health += 1

        # eat fellow creatures
        if (self.attacking and
            nearest.x - 24 < self.x < nearest.x + 24 and
            nearest.y - 24 < self.y < nearest.y + 24):
            other_creatures[other_creatures.index(nearest)].health -= 1
            if other_creatures[other_creatures.index(nearest)].health <= 0:
                other_creatures.remove(other_creatures[other_creatures.index(nearest)])
                self.health += 4
                if self.health > self.max_health: self.health = self.max_health

        self.label = pyglet.text.Label(str(int(self.health)),
                  font_name='Times New Roman',
                  font_size=16,
                  x=self.x, y=self.y,
                  anchor_x='center', anchor_y='center')

        self.health -= 0.1

    def give_birth(self):
        global creatures
        if self.health >= self.max_health / 2 and "random.random() > 0.7":
            creatures.append(Creature(
                self.mutability_chance, self.creature_number, self.relative_max_health/2,
                self.relative_speed, mutation.mutate(self.dna),
                random.randint(16, window_width - 16),
                random.randint(16, window_height - 16)
                ))
            self.health = self.health//2

