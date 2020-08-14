def diag_1_sym(s):
    t = []
    for x in s.split():
        for i,y in enumerate(x):
            if len(t) < i + 1:
                t.append(y)
            else:
                t[i] = t[i] + y
    return '\n'.join(t)

def rot_90_clock(strng):
    return '\n'.join([''.join([y for y in x][::-1]) for x in diag_1_sym(strng).split()])

def selfie_and_diag1(s):
    return '\n'.join([x+'|'+y for i,x in enumerate(s.split()) for r,y in enumerate(diag_1_sym(s).split()) if i == r])