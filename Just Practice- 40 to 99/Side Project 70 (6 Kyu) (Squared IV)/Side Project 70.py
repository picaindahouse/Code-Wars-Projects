def oper(fct, s):
    t = []
    for x in s.split():
        for i,y in enumerate(x):
            if len(t) < i + 1:
                t.append(y)
            else:
                t[i] = t[i] + y
    return fct('\n'.join(t), s)

def rot_90_counter(s, y):
    return '\n'.join([x for x in s.split()] [::-1])
  
def diag_2_sym(s, y):
    return '\n'.join([''.join([y for y in x][::-1]) for x in rot_90_counter(s,y).split()])

def selfie_diag2_counterclock(s, og):
    return '\n'.join([x+'|'+y+'|'+z for i,x in enumerate(og.split()) for r,y in enumerate(diag_2_sym(s, 2).split()) for h,z in enumerate(rot_90_counter(s, 2).split()) if i == r and r == h and i == h])
