def reverse(seq):
    sim = list(enumerate(seq))
    seq.clear()
    sim.sort(reverse = True)
    for i,x in sim:
        seq.append(x)