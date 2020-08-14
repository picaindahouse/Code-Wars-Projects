def find_in_array(seq, predicate):
    return next((i for i,x in enumerate(seq) if predicate(x,i) == True), -1)