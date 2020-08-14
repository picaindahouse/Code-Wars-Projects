def persistence(n):
    import numpy
    Round = 0 
    while len(str(n)) > 1:
        n = numpy.prod([int(x) for x in str(n)])
        Round = Round + 1
    return Round