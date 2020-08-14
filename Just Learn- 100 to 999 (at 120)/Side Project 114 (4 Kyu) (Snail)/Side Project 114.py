def snail(array):
    pos, tom, tim = [0,0], [len(x) for x in array], []
    tam, up = len(tom) -1, 0
    while len(tim) != sum(tom):
        tim.append(array[pos[0]][pos[1]])
        array[pos[0]][pos[1]] = '?'
        if pos[1] == up and pos[0] != up:  
            pos[0] -= 1
            if array[pos[0]-1][pos[1]] == '?':
                tam -= 1
                up += 1
        elif pos[1] < tom[0]-1 and array[pos[0]][pos[1]+1] != '?': pos[1] += 1
        elif pos[0] < tam and array[pos[0]+1][pos[1]] != '?': pos[0] += 1
        elif pos[0] == tam: pos[1] -= 1
    return tim