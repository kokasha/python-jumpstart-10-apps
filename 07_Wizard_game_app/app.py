import random

import time

from players import Wizard, Creature


def main():
    print_header('Wizard Game App')
    paly_game_loop()


def paly_game_loop():
    creatures = [
        Creature('Tod', 5),
        Creature('Tiger', 30),
        Creature('Bat', 20),
        Creature('Evil Wizard', 100),
        Creature('Dragon', 50)
    ]

    hero = Wizard('Gandelf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared'
              .format(active_creature.name,active_creature.level))
        print()

        cmd = input('Do you want to [a]ttack, [r]unaway or [l]ook around: ').lower()

        if cmd == 'a':
            print('Attack ...')
            result = hero.attack(active_creature)

            if result:
                print('\nWizard Has WON')
                creatures.remove(active_creature)

            else:
                print('Wizard has been defeated and needs to rest')
                time.sleep(5)
                print('Wizard Returns Active as before')

        elif cmd == 'r':
            print('Run ...')
        elif cmd == 'l':
            print('{} takes a look around and finds:'.format(hero.name))
            for c in creatures:
                print('* {} of level {}'.format(c.name,c.level))
        else:
            print("We didn't get your Input {}".format(cmd.lower()))
            print("Qutting the Game ....")
            break

        print()

    pass


def print_header(app_name):
    print('-' * 30)
    print('{:^30}'.format(app_name))
    print('-' * 30)


if __name__ == "__main__":
    main()
