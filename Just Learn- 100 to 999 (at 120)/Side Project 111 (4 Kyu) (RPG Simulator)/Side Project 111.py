def rpg(field,actions):
    Health, Atk, Def, Bag, tom, coin, Map, enemy, demon, level, evil, Demon = 3,1,1,[], '><^v', 0, [[d for d in e] for e in field], [1,2], [10,3], 0, [], 'hey'
    
    for i,x in enumerate(field):
        for r,y in enumerate(x):
            if y in tom: pos, main = [i,r], y
            elif y in 'E': evil.append([i,r])
            elif y in 'D': Demon = [i,r]
    
    for z in actions:
        movement = {'>': [pos[0],pos[1] + 1], '<': [pos[0],pos[1] - 1], '^': [pos[0] - 1,pos[1]], 'v': [pos[0] + 1,pos[1]] }
        
        if z == 'F':
            Map[pos[0]][pos[1]] = ' '
            pos = movement[main]
            if pos[0] < 0  or pos[0] > len(Map) - 1 or pos[1] < 0 or pos[1] > len(Map[0]) - 1: return None
            elif Map[pos[0]][pos[1]] in '#M-|ED': return None
            elif Map[pos[0]][pos[1]] in 'CKH': 
                Bag.append(Map[pos[0]][pos[1]])
                Bag.sort()
            elif Map[pos[0]][pos[1]] == 'S': Def += 1
            elif Map[pos[0]][pos[1]] == 'X': Atk += 1
            Map[pos[0]][pos[1]] = main
        
        elif z in tom: main, Map[pos[0]][pos[1]] = z, z
            
        elif z in 'KCH':
            future = movement[main]
            if z not in Bag: return None
            if z == 'H' and Health < 3: Health = 3
            elif z == 'K' and Map[future[0]][future[1]] in '-|': Map[future[0]][future[1]] = ' '
            elif z == 'C' and Map[future[0]][future[1]] == 'M':
                coin += 1
                if coin == 3: 
                    Map[future[0]][future[1]] = ' '
                    coin = 0
            else: return None
            Bag.remove(z)
        
        else:
            future = movement[main]
            if Map[future[0]][future[1]] not in 'ED': return None
            elif Map[future[0]][future[1]] == 'E': 
                Map[future[0]][future[1]] = ' '
                evil.remove(future)
                level += 1
                if level % 3 == 0: Atk += 1
            else:
                demon[0] = demon[0] - Atk
                if demon[0] <=0 : Map[future[0]][future[1]], demon = ' ', [0,0]
                                                
        scan = [movement['>'],movement['<'],movement['^'],movement['v']]
        for h in scan:
            if h in evil: Health = Health - max(0, enemy[1] - Def)
            elif h == Demon: Health = Health - max(0, demon[1] - Def)
            if Health <= 0: return None
            
    return (Map, Health, Atk, Def, Bag)