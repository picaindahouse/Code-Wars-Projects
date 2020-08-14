def count_adjacent_pairs(st): 
    tim, tam, tum = (st.lower()).split(), [], []
    [tam.append([0,x]) if not tam or x != tam[-1][1] else tam.append([1,x]) for x in tim]
    [tum.append([i,x]) for i,x in tam if i == 1 and not tum or i == 1 and [i,x] != tum[-1]]
    return len(tum)