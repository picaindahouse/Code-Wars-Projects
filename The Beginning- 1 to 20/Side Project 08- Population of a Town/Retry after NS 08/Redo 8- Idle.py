def nb_year(p0, percent, aug, p):
    year = 0
    while p > p0:
        p0 = int(p0/100*(100 + percent)) + aug
        year = year + 1
    return year