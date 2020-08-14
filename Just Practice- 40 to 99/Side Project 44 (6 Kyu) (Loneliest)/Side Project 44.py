def lonely (n,w,y):
    return (sum([int(x) for (i,x) in enumerate(str(y)) if (i - n) <= w and (i - n) > 0 or (n - i) <= w and (n-i) > 0]), w)
def loneliest(y): 
    tom = [lonely(i,int(x),y) for i,x in enumerate(str(y))]
    return True if 1 in [x for i,x in sorted(tom) if i == sorted(tom)[0][0]] else False