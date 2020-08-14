def differentiate(tom, point):
    tam, tim = [x.split('-') for x in tom.split('+')], []
    for x in tam:
        for i,y in enumerate(x):
            if 'x' not in y: tim.append(0)
            else: 
                if '^' not in y: 
                    if i == 0: tim.append(int(y.replace('x',''))) if len(y) > 1 else tim.append(int(y.replace('x','1')))
                    else: tim.append(-int(y.replace('x',''))) if len(y) > 1 else tim.append(-int(y.replace('x','1')))
                else:
                    yo = y.find('^')
                    pls, sim = y[0:yo + 1] + str(int(y[yo + 1:]) -1), int(y[yo + 1:])
                    if i == 0: tim.append(sim * eval(pls.replace('^','**').replace('x','*'+str(point)))) if y.find('x') != 0 else tim.append(sim * eval(pls.replace('^','**').replace('x',str(point)))) 
                    else: tim.append(sim * -eval(pls.replace('^','**').replace('x','*('+str(point)+')'))) if y.find('x') != 0 else tim.append(sim * -eval(pls.replace('^','**').replace('x','('+str(point)+')')))
    return sum(tim)