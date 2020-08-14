def recoverSecret(triplets):
    zim = []
    [[zim.append(y) for y in x if y not in zim]for x in triplets]
    cool = dict(zip(zim,[[] for h in range(len(zim))]))
    [[[cool[e].append(w) for w in r[r.index(e)+1:] if w not in cool[e]] for e in r]for r in triplets]
    [[[cool[d].append(q) for q in cool[i] if q not in cool[d]] for i in cool[d]] for d in cool]
    return ''.join(sorted(cool, key= lambda x: len(cool[x]), reverse=True))