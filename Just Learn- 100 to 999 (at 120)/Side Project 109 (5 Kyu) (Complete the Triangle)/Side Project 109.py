def make_triangle(m,n):
    sim = 0
    for x in range(1,1000):
        sim += x
        if (n-m+1) == sim: break
        elif (n-m+1) < sim: return ''
    Max, pos, simp, z = 2 * x - 1, [0,x-1], 0, [x][0] 
    tom = [[str(' ') for z in range((Max - (x - (y + 1))))] for y in range(x)]
    tom[pos[0]][pos[1]] = str(m)[-1]
    while m < n:
        if pos[1] == 0 + (x-(pos[0]+1)) + simp and pos[0] != 2* (z-x) :
            pos[0] -= 1
            pos[1] += 1
            
        elif pos[0] < x-1: 
            pos[0] += 1
            pos[1] += 1
            
        elif pos[0] == x-1 and pos[1] != 0 + (x-(pos[0]+1)): pos[1] -= 2
            
        m += 1
        if tom[pos[0]][pos[1]] == ' ':  tom[pos[0]][pos[1]] = str(m)[-1]
        else:           
            simp, x, pos[0] = simp + 3, x - 1, pos[0] + 2
            tom[pos[0]][pos[1]] = str(m)[-1]
    [z.insert(0,'\n') for z in tom if z != tom[0]]
    return ''.join([''.join(z) for z in tom])