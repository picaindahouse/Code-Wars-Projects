import math
def sum_arrangements(num):
    num = str(num)
    return sum([num.count(x) * int(x*len(num)) for x in '123456789']) * math.factorial((len(str(num)) - 1))