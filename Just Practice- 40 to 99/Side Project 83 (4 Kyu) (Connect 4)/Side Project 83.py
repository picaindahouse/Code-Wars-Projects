from numpy import diagonal
def who_is_winner (tom):
    tim = [[x for x in str(0)*7] for x in range(6)]
    for x in tom:
        count, tum, master = 5, [], []
        loc = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}[x[0]]
        while tim[count][loc] != '0':
            count -= 1
        tim[count][loc] = x[2:]
        if tim[count].count(x[2:]) >= 4:
            master.append(tim[count])    
        if [tim[x][loc] for x in range(6)].count(x[2:]) >= 4:
            master.append([tim[x][loc] for x in range(6)])
        if list(diagonal(tim, (loc + 1) - (6-(5-count)))).count(x[2:]) >= 4:
            master.append(list(diagonal(tim, (loc + 1) - (6-(5-count)))))
        [x.reverse() for x in tim]
        counte = 6 - loc
        if list(diagonal(tim, (counte + 1) - (6-(5-count)))).count(x[2:]) >= 4:
            master = list(diagonal(tim, (counte + 1) - (6-(5-count))))
        [x.reverse() for x in tim]   
        if master:
            for y in master:   
                for x in y:
                    if not tum or x != tum[-1][0]:
                        tum.append([x,1])
                    else:
                        tum[-1][1] += 1
                if [x[1] for x in tum if x[0] == 'Yellow' and x[1] >= 4]:
                    return 'Yellow'
                elif [x[1] for x in tum if x[0] == 'Red' and x[1] >= 4]:
                    return 'Red' 
                else: tum = []
    return 'Draw'