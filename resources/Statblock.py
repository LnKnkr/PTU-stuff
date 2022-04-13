

class StatBlock:
    def __init__(self):
        self.attack = 0
        self.defense = 0
        self.sp_attack = 0
        self.sp_defense = 0
        self.speed = 0
        self.kp = 0

    def insert_values(self, attack, defense, sp_attack, sp_defense, speed, kp):
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.kp = kp

