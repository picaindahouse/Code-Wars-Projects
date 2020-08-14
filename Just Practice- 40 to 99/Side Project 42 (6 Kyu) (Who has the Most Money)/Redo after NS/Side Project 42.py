class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

def money(student):
     return (5 * student.fives + 10 * student.tens + 20 * student.twenties, student.name)

def most_money(students):
    return [x for i,x in [money(x) for x in students] if i == max([money(x) for x in students])[0]][0] if len([x for i,x in [money(x) for x in students] if i == max([money(x) for x in students])[0]]) == 1 else 'all'
