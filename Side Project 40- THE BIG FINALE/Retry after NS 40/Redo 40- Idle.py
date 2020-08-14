def mixed_fraction(s):
    tom = s.replace('/',' ') if s.count('-') < 2 else (s.replace('/',' ')).replace('-','')
    tim = [x for x in tom.split()]
    if tom.count('-') > 0:
        if tim[1].count('-') > 0:
            tim[1] = tim[1].replace('-','')
        elif tim[0].count('-') > 0:
            tim[0] = tim[0].replace('-','')
        minus = 'yes'
    else:
        minus = 'no'
    main = int(int(tim[0])/int(tim[1]))
    if int(tim[0])/int(tim[1]) % 1 == 0:
        if str(main) == '0':
            return '0'
        return '-' + str(main) if minus == 'yes' else str(main)
    bottom = int(tim[1])
    top = int(tim[0]) - main*bottom
    from fractions import Fraction
    Fraction(top, bottom)
    if main == 0:
        return '{}{}{}'.format('-' if minus == 'yes' else '', Fraction(top,bottom).numerator, '/' + str(Fraction(top,bottom).denominator))
    return '{}{} {}{}'.format('-' if minus == 'yes' else '',main if main != 0 else '',Fraction(top,bottom).numerator if Fraction(top,bottom).numerator != 0 else '0','/' + str(Fraction(top,bottom).denominator) if Fraction(top,bottom).numerator != 0 else '')