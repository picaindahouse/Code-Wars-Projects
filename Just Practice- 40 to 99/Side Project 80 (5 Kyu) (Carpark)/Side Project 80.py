def escape(carpark):
    tom, escape = [], 0
    position = [[[r,i] for i,y in enumerate(x) if y == 2] for r,x in enumerate(carpark) if [[r,i] for i,y in enumerate(x) if y == 2]][0][0]
    while escape != 1:
        if 1 in carpark[position[0]]:
            stair = [i for i,x in enumerate(carpark[position[0]]) if x == 1][0]
            if position[1] - stair > 0:
                tom.append('L' + str(position[1] - stair)), tom.append('D1')
                floor = 1
            elif position[1] - stair < 0:
                tom.append('R' + str(abs(position[1] - stair))), tom.append('D1')
                floor = 1
            else: 
                floor += 1
                tom[-1] = 'D' + str(floor)
            position[0],position[1] = position[0] + 1, stair
        else:
            if position[1] - (len(carpark[0]) - 1) > 0:
                tom.append('L' + str(position[1] - (len(carpark[0]) - 1)))
            elif position[1] - (len(carpark[0]) - 1) < 0:
                tom.append('R' + str(abs(position[1] - (len(carpark[0]) - 1))))
            escape = 1
    return tom