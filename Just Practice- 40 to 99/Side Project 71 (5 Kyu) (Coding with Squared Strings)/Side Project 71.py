def diag_1_sym(s):
    t = []
    for x in s.split('\n'):
        for i,y in enumerate(x):
            if len(t) < i + 1:
                t.append(y)
            else:
                t[i] = t[i] + y
    return '\n'.join(t)

def rot_90_clock(strng):
    return '\n'.join([''.join([y for y in x][::-1]) for x in diag_1_sym(strng).split('\n')])

def rot_90_counter(s):
    return '\n'.join([x for x in diag_1_sym(s).split('\n')] [::-1])

def code(s):
    n = [x for x in range(20) if x*x>len(s)][0]
    r = [x for x in s]
    [r.append(chr(11)) for x in range(n*n-len(s))]
    [r.insert(n*(x+1)+x,'\n')  for x in range(n-1)]
    return rot_90_clock(''.join(r)) if s else ''

def decode(s):
    s = rot_90_counter(s)
    return ''.join([''.join(''.join(x.split('\n')).split(chr(11))) for x in s.split('\n')])