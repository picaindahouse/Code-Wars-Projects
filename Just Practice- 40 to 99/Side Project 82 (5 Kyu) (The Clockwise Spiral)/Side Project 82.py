def create_spiral(n):
    if type(n) != int or n < 1:
        return []
    swirl,position = [[int(y) for y in str(0)*n] for x in range(n)], [0,0]
    tom = 1
    for x in range(1,n**2 + 1):
        if swirl[position[0]][position[1]] == 0:
            swirl[position[0]][position[1]] = x
        if position[0] > 0 and swirl[position[0] - 1][position[1]] == 0 and tom == 1:
            position[0] -= 1
        elif position[1] < n-1 and swirl[position[0]][position[1] + 1] == 0 and tom == 1:
            position[1] += 1
        elif position[0] < n-1 and swirl[position[0] + 1][position[1]] == 0 and tom == 1:
            position[0] += 1
        elif position[1] > 0:
            position[1] -= 1
            tom += 1
            if swirl[position[0]].count(0) == 1:
                tom = 1    
    return swirl