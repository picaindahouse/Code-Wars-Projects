def interpreter(tom):
    level, floor, p, word = 0, [], 0, []
    for x in tom:
        if x == '>':
            print(level,floor)
            if level == len(floor):
                floor.append((level,p))
                p = 0
                level += 1
            elif level + 1 == len(floor):
                floor.append((level,p))
                p = 0
                level += 1
            else:
                floor[level] = (level,p)
                level += 1
                p = floor[level][1]
        elif x == '<':
            if level <= 0:
                floor.append((level,p))
                level -= 1
                p = 0
            elif level == len(floor):
                floor.append((level,p))
                level -= 1
                p = floor[level][1]
            else:
                floor[level] = (level,p)
                level -= 1
                p = floor[level][1]
        elif x == '+':
            p += 1
        else:
            word.append(chr(p))
            print (word)
    return(''.join(word))