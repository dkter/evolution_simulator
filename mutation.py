import dna_parser
import random
#from random_creature import write_formula


def mutate(dna):
    #mutation_chance, creature_number, max_health, speed, dna\
    #    = dna_parser.splitDNA(dna)

    blocks = []

    while dna != '':
        char = dna[0]
        if char.isdigit():
            tempNumber = 0
            num = ''
            while tempNumber < len(dna) and dna[tempNumber].isdigit():
                tempNumber += 1
            num += str(int(dna[:tempNumber]))
            #print(num)
            blocks.append(num)
            dna = dna[tempNumber:]
            tempNumber=0
        else:
            blocks += char
            dna = dna[1:]

    #print(blocks)

    dna_index = random.randint(0, len(blocks)-1)
    dna_block = blocks[dna_index]

    new_dna = ""




    # dna_index = random.randint(0, len(dna)-1)
    # if dna[dna_index].isdigit():
    #     tempNumber = 0
    #     tempNumber2 = 0
    #     num = ""
    #     while dna_index + tempNumber < len(dna) and dna[dna_index + tempNumber].isdigit():
    #         tempNumber += 1
    #         print(tempNumber)
    #     while dna_index - tempNumber2 > 0 and dna[dna_index - tempNumber2].isdigit():
    #         tempNumber2 -= 1
    #         print(tempNumber2)
    #     num = str(dna[tempNumber2:dna_index]) + str(dna[dna_index:tempNumber])
        
    #     #mutate_number(int(num))

    #     print(num)

    # dna_block = dna[dna_index]
    # new_dna = dna

    thing = dna_block

    if dna_block.isdigit():
        thing = mutate_number(int(dna_block))
    elif dna_block in ('x', 'X', 'f'):
        thing = mutate_x(dna_block)
    elif dna_block in ('y', 'Y', 'F'):
        thing = mutate_y(dna_block)
    elif dna_block in ('+', '-', '*', '/', '%'):
        thing = mutate_operator(dna_block)
    elif dna_block in ('=', '!', '<', ',', '>'):
        thing = mutate_comparator(dna_block)
    elif dna_block in ('U', 'D', 'L', 'R'):
        thing = mutate_vote(dna_block)
    elif dna_block in ('x', 'y', 'z', 'c', 'h', 'q', 'w'):
        thing =  mutate_property(dna_block)
    elif dna_block in ('X', 'Y', 'p', 'S', 'C', 'A', 'H', 'Q', 'W'):
        thing = mutate_nearest(dna_block)
    elif dna_block in ('f', 'F', 'P'):
        thing = mutate_food(dna_block)
    elif dna_block in ('&', '|'):
        thing = mutate_logic(dna_block)
    elif dna_block == ';':
        thing = mutate_semicolon(dna_block)

    if random.choice(range(0,10))==0:
        add_if(dna,len(dna)-1)

    new_dna = ''.join(blocks[:dna_index]) + str(thing) + ''.join(blocks[dna_index+1:])
   
    return new_dna

    # index = 0
    # while index < len(dna):
    #     char = dna[index]
    #     if char.isdigit():
    #         tempNumber = 0
    #         num = ""
    #         while index + tempNumber < len(dna) and dna[index + tempNumber].isdigit():
    #             tempNumber += 1
    #         num += str(int(dna[:tempNumber]))
    #         index = tempNumber
    #         mutate_number(int(num))
    #     elif char in ('+', '-', '*', '/', '%'):
    #         mutate_operator(char)
    #     elif char in ('=', '!', '<', ',', '>'):
    #         mutate_comparator(char)
    #     elif char in ('U', 'D', 'L', 'R'):
    #         mutate_vote(char)
    #     elif char in ('&', '|'):
    #         # I'm doing this wrong; do like key-value pairs or something


def mutate_number(number):
    nums = ([str(i) for i in range(number - 10, number + 10)]*5 +
            [str(random.randint(0,9999)),'x', 'y', 'X', 'Y', 'p', 'f', 'F', 'P', 'z', 'S',
             'c', 'C', 'A', 'h', 'H', 'q', 'Q', 'w', 'W'])
    x = random.choice(nums)

    if isinstance(x, int) and int(x) < 1:
        x = "1"
    return x


def mutate_operator(operator):
    return random.choice(('+', '-', '*', '/', '%'))


def mutate_comparator(comparator):
    return random.choice(('=', '!', '<', ',', '>'))


def mutate_vote(vote):
    return random.choice(('U', 'D', 'L', 'R'))


def mutate_logic(logic):
    return random.choice(('&', '|'))


def mutate_semicolon(semicolon):
    return ''


def mutate_action(action):
    if random.random() > 0.7:
        x = ';'
    else:
        x = ''
    return x + random.choice(('b', 'a', 's'))


def mutate_x(x):
    return random.choice(('x', 'X', 'f'))


def mutate_y(y):
    return random.choice(('y', 'Y', 'F'))


def mutate_property(property):
    return random.choice(('x', 'y', 'z', 'c', 'h', 'q', 'w'))


def mutate_nearest(property):
    return random.choice(('X', 'Y', 'p', 'S', 'C', 'A', 'H', 'Q', 'W'))


def mutate_food(property):
    return random.choice(('f', 'F', 'P'))

def add_parameter():
    return random.choice(('+','-','*','/','%'))+write_formula()

#print(mutate ("032012460401aif<x:L1lf>x:R1;iF<y:D1lF>y:U1"))