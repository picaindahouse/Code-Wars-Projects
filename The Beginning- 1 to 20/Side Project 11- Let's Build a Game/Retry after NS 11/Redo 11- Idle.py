class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1.name:
        defend = fighter2
        first_attacker = fighter1
    else:
        defend = fighter1
        first_attacker = fighter2
    Round = 1
    while fighter1.health > 0 and fighter2.health > 0:
        if Round%2 != 0:
            defend.health = defend.health - first_attacker.damage_per_attack
        else:
            first_attacker.health = first_attacker.health - defend.damage_per_attack
        Round = Round + 1
    return first_attacker.name if first_attacker.health > 0 else defend.name