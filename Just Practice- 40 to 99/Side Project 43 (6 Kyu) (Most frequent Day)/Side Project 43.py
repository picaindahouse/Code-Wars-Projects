week = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
import calendar
def last (year):
    tom = calendar.monthrange(year,12)
    tim = (tom[0] + (tom[1]-1 % 7)) % 7
    return week[tim]

def Max (year):
    xtra_1 = week[0:week.index(last(year))+1]
    xtra_2 = week[week.index(last(year-1))+1:] if year - 1 > 0 else []
    tom = [x for x in xtra_1 if x in xtra_2]
    [xtra_1.append(x) for x in xtra_2]
    return tom if tom else xtra_1