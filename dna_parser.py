import re
import math

dna=''
curDNA=''
listOfCode={
    'i': '\nif ',#
    'l': '\nelif ',#
    '&': ' and ',#
    '|': ' or ',#
    ':': ':',#
    ';': '',#
    'x': ' self.x ',#
    'y': ' self.y ',#
    'X': ' nearest.x ',#
    'Y': ' nearest.y ',#
    'p': ' distance(you, nearest) ',#
    'f': ' nearest_food.x ',#
    'F': ' nearest_food.y ',#
    'P': ' distance(you, nearest_food) ',#
    'z': ' self.signal ',#
    'S': ' nearest.signal ',
    'c': ' self.creature_number ',#
    'C': ' nearest.creature',#_number ',#
    'A': ' nearest.attacking ',#
#   't': ' self.timer ',
    'h': ' self.health ',#
    'H': ' nearest.health ',#
    'q': ' self.speed ',#
    'Q': ' nearest.speed ',#
    '+': '+',#
    '-': '-',#
    '*': '*',#
    '/': '/',#
    '%': '%',#
    '=': '==',#
    '!': '!=',#
    '<': '<',#
    ',': '<=',#
    '>': '>',#
    '.': '>=',#
    'U': '\nself.votes["up"] += ',#
    'L': '\nself.votes["left"] += ',#
    'R': '\nself.votes["right"] += ',#
    'D': '\nself.votes["down"] += ',#
#   'T': '\nself.timer = ',
    'b': '\nself.give_birth()',
    'a': '\nself.attacking = True',#
    's': '\nself.signal = '}#


beginning_re = re.compile(r'''
    (?P<mutation_chance> \d\d\d)
    (?P<creature_number> \d\d\d\d)
    (?P<max_health>      \d\d)
    (?P<speed>           \d\d)
    ''', re.X)


def splitDNA(dna):
    beginning = dna[:11]
    dna = dna[11:]

    match = re.match(beginning_re, beginning)

    mutation_chance = int(match.group("mutation_chance"))
    creature_number = int(match.group("creature_number"))
    max_health = int(match.group("max_health"))
    speed = int(match.group("speed"))

    return (mutation_chance, creature_number, max_health,
            speed, dna)


def parse_dna(dna, creatures):
    tempNumber = 0
    char = dna[0]
    code = ''
    indentation = 0

    while dna != '':
        char = dna[0]
        if char.isdigit():
            while tempNumber < len(dna) and dna[tempNumber].isdigit():
                tempNumber += 1
            code += str(int(dna[:tempNumber]))
            dna = dna[tempNumber:]
            tempNumber=0
        else:
            if char == ";":
                indentation -= 1
            else:
                if listOfCode[char][0] == '\n':
                    if char == "l":
                        indentation -= 1
                    code += '\n' + ('    ' * indentation) + listOfCode[char][1:]
                else:
                    code += ('    ' * indentation) + listOfCode[char]
                if char == ":":
                    indentation += 1
            dna = dna[1:]

    # prettify code
    # for i in code.split('\n'):
    #     if '    ' in code.lstrip():
    #         code = 2

    return code


def distance(a, b):
    return math.sqrt(
        (b.x - a.x) ** 2 +
        (b.y - a.y) ** 2)


def nearest(creature, other_creatures):
    distances = {}
    for i in other_creatures:
        distances[i] = distance(i, creature)
    return min(distances, key=distances.get)
# import creature
# bob = creature.Creature(1,1,1,1,1,1,1, 50, 50)
# not_bob = [
#     creature.Creature(1,1,1,1,1,1,1, 53, 52),
#     creature.Creature(1,1,1,1,1,1,1, 140, 179),
#     creature.Creature(1,1,1,1,1,1,1, 55, 55),
#     creature.Creature(1,1,1,1,1,1,1, 0, 50)
# ]

# c = nearest(bob, not_bob)
# print(c.x, c.y)

#print(parse_dna("032012460401aif<x:L1lf>x:R1;iF<y:D1lF>y:U1b", []))
