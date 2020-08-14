def uniq_c(seq): 
    tum, count = [], 1
    for x in seq:
        if not tum or x != tum[-1][0]:
            count = 1
            tum.append([x,count])
        else:
            count += 1
            tum[-1] = [x, count]
    return [(i,x) for i,x in tum]