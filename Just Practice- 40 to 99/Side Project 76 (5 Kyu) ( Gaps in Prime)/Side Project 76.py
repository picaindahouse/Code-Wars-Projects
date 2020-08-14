def gap(g, m, n):
    tim,tom = [1.1],0
    for x in range(m,n+1):
        if x in [1,2,3,5,7,9,11,13,15,17,19] : 
            tim.append(x)
            if tim[-1] - tim[-2] == g:
                return[tim[-2],tim[-1]]
        elif x % 2 == 0:
            shag = 2
        elif x % 3 == 0:
            shag = 3
        elif x % 5 == 0:
            shag = 5
        elif len([y for y in [2,3,5,7,9,11,13,15,17,19] if x%y == 0]) > 0:
            shag = 2
        else:
            for y in range(21,int(x/20),2):
                if x%y == 0:
                    tom = 1
                    break
                else:
                    tom = 0
            if tom == 0:
                tim.append(x)
                if tim[-1] - tim[-2] == g:
                    return[tim[-2],tim[-1]]
    return None