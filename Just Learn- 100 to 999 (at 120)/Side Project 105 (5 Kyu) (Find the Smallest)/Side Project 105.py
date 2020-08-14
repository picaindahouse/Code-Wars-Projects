def smallest(n):
    sam, tim, plim, sim = [int(x) for x in str(n)],[],[x for x in str(n)],[]
    for i,x in enumerate(sam): 
        if sam[0] < x: 
            plim.insert(i-1, plim.pop(0))
            print(plim)
            sim.append([int(''.join(plim)), 0, i-1])
            break
    if not sim: 
        plim.insert(len(plim)-1, plim.pop(0))
        sim.append([int(''.join(plim)), 0, len(plim)-1])
        
    for y in range(len(sam)):
        for i,x in enumerate(sam): 
            if x < sam[y] and i > y: tim.append([i,y])
        if tim: break   
    for i,x in tim:
        plim = [x for x in str(n)]
        plim.insert(x,plim.pop(i))
        if x == 1 and plim[1] == plim[0]: x = 0
        sim.append([int(''.join(plim)), i, x])
    
    return sorted(sim)[0]