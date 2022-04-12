import Typing


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
    def __init__(self):
        self.attack = 0
        self.defense = 0
        self.sp_attack = 0
        self.sp_defense = 0
        self.speed = 0
        self.kp = 0
        self.type = 1


def calculate_mod(attacker, defendant):
    pass


def main():
    x = CalculateDamagePTU(10, 4, 1.1)
    print(x.damage())


main()
