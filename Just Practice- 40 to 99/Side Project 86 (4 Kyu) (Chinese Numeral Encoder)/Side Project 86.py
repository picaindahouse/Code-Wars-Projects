def to_chinese_numeral(n):
    numerals = {"-":"负", ".":"点", 0:"零", 1:"一", 2:"二", 3:"三", 4:"四", 5:"五", 6:"六", 7:"七", 8:"八", 9:"九", 10:"十", 100:"百", 1000:"千", 10000:"万"}
    him, blue = 1, 1
    if n < 0: n, him = abs(n), 4
    if n % 1 != 0: t,n, blue = n,int(n), 4
    tim,tam, tom, tym = [], [x for x in str(n)], [], []
    tam.reverse()
    [tim.append((x)) if not tim and x != '0' or True in [y in tim  for y in ['1','2','3','4','5','6','7','8','9']] or x in '.123456789' else tim.append((1,x))   for x in tam]
    tim.reverse()
    for i,x in enumerate(tim):
        yo = int('1' + '0' * (len(str(n)) - i))
        if not tom: 
            if x == (1,'0'):
                tom.append(numerals[0])
            else: tom.append(numerals[int(x)])
        elif n > 9 and n < 20:
            tom = []
            tom.append(numerals[yo])
            if x != (1,'0'):
                tom.append(numerals[int(x)])
        elif x == (1,'0'): 
            if tom[-1] not in [numerals[100],numerals[1000],numerals[10000]]:
                tom.append(numerals[yo])
        else: 
            if tom[-1] != numerals[0]:
                tom.append(numerals[yo])
                tom.append(numerals[int(x)])
            elif tom[-1] == numerals[0] and x == '0': 1
            else:   tom.append(numerals[int(x)])
    if him == 4: tom.insert(0, numerals['-'])
    if blue == 4:
        [tym.append(x) for x in str(t) if x == '.' or '.' in tym]
        print(tym)
        for y in tym:
            if y in '.0123456789':
                tom.append(numerals[y]) if y == '.' else tom.append(numerals[int(y)])
    return ''.join(tom) 