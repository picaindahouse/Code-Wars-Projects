def smth (n,m):
    count = 0
    while count != len(str(n))%4 +1:
        if sum([int(x) for x in str(n)][count:count + 4]) > m:
            return None
        count += 1
    return n

def max_sumDig(nMax, maxSum):
    tom = [smth(x, maxSum) for x in range(1000, nMax + 1) if smth(x, maxSum) != None]
    return [len(tom), sorted([[abs(sum(tom)/len(tom) - x) ,x] for x in tom])[0][1], sum(tom)]


