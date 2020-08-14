class robot:
    def __init__(self, name,health, speed, tactics):
        self.name = name
        self.health = health
        self.speed = speed
        self.tactics = tactics
        self.n = 0 if self.tactics else -1
    def attack (self, other, damage):
        if self.n >= 0:
            other.health -= damage[self.tactics[self.n]]
            self.n += 1
        if self.n == len(self.tactics): self.n = -1
            
def fight (r1, r2, tactics):
    ro1 = robot(r1['name'],r1['health'],r1['speed'],r1['tactics'])
    ro2 = robot(r2['name'],r2['health'],r2['speed'],r2['tactics'])
    if ro1.speed > ro2.speed or ro1.speed == ro2.speed: tom, tim = ro1, ro2
    else: tom, tim = ro2, ro1
    while ro1.health > 0 and ro2.health > 0:
        if tom.n < 0 and tim.n < 0:
            if ro1.health - ro2.health == 0: return "The fight was a draw."
            else: return "{} has won the fight.".format(ro1.name if ro1.health > ro2.health else ro2.name)
        tom.attack(tim, tactics)
        tom,tim = tim,tom
    return "{} has won the fight.".format(ro1.name if ro1.health > 0 else ro2.name)