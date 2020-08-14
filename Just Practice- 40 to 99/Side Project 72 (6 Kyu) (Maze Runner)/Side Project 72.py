def maze_runner(maze, directions):
    position = [[[r,i] for i,y in enumerate(x) if y == 2] for r,x in enumerate(maze) if [(r,i) for i,y in enumerate(x) if y == 2]][0][0]
    for x in directions:
        try:
            if x == 'N': position[0] = position[0] - 1
            elif x == 'S': position[0] = position[0] + 1
            elif x == 'E': position[1] = position[1] + 1
            else: position[1] = position[1] - 1
            if maze[position[0]][position[1]] == 3: return 'Finish'
            elif maze[position[0]][position[1]] == 1 or position[0] < 0 or position[1] < 0:return 'Dead'
        except IndexError: return 'Dead'
    if maze[position[0]][position[1]] == 0 or maze[position[0]][position[1]] == 2: return 'Lost'