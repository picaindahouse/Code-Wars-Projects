class Fraction(object):

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
    
    def __add__ (self, other):
        tim, tom = self.bottom * other.bottom, self.bottom * other.top + other.bottom * self.top
        tam = [x for x in range(1,tim) if tom%x == 0  and tim%x == 0]
        tom, tim = int(tom/max(tam)), int(tim/max(tam))   
        return Fraction(tom,tim)
    def __str__ (self):
        return str(self.top) + '/' + str(self.bottom)