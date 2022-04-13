from resources.Statblock import StatBlock
from resources.Typing import PokemonType


class CalculateDamagePTU:
    # Attack Damage
    # Defense Stat
    # Modification

    def __init__(self, attack, defense, mod):
        self.attack = attack
        self.defense = defense
        self.mod = mod

    def damage(self):
        pivot = self.attack * self.mod
        pivot = pivot - self.defense
        if pivot <= 0:
            return 1
        else:
            return pivot

    def change_values(self, attack, defense, mod):
        self.attack = attack
        self.defense = defense
        self.mod = mod


class Unit:
    def __init__(self, stats, type):
        self.stats = StatBlock()
        self.type = PokemonType(type)
        self.stats.insert_values(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5])


def calculate_mod(attacker, defendant):
    pass


def main():
    x = CalculateDamagePTU(10, 4, 1.1)
    print(x.damage())


main()
