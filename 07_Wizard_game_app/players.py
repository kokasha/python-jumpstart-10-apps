import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature Object with name {} at level {}".format(self.name, self.level)

    def get_roll(self):
        roll = self.level * random.choice(range(1, 10))
        print('{} Rolled {}'.format(self.name, roll))
        return roll


class Wizard(Creature):

    def attack(self, creature):
        print('{} attacks {}\n'.format(
                self.name, creature.name))

        my_roll = self.get_roll()
        creature_roll = creature.get_roll()

        if my_roll >= creature_roll:
            return True
        else:
            return False
