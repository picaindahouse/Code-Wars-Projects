def highlight(code):
    tom = []
    for x in code:
        if tom and len(tom[-1]) > 3 and x == tom[-1][3]: tom[-1][1] = tom[-1][1] + x
        elif tom and len(tom[-1]) > 3 and x in '0123456789' and tom[-1][3] in '0123456789': tom[-1][1] = tom[-1][1] + x
        elif x == 'F': tom.append(['<span style="color: pink">',x,'</span>',x])
        elif x == 'L': tom.append(['<span style="color: red">',x,'</span>',x])
        elif x == 'R': tom.append(['<span style="color: green">',x,'</span>',x])
        elif x in '0123456789' : tom.append(['<span style="color: orange">',x,'</span>',x])
        else: tom.append(x)
    return ''.join([''.join(x[0:3]) for x in tom])