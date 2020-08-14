tom = [45,54]
def sum_dif_rev(n):
    global tom
    try: return tom[n-1]
    except IndexError:
        while len(tom) < n:
            for x in range(tom[-1] + 1, 100000000):
                if x%10 == 0: pass
                elif x - int(''.join([y for y in str(x)][::-1])) ==0: pass
                elif (x + int(''.join([y for y in str(x)][::-1]))) % abs(x - int(''.join([y for y in str(x)][::-1]))) == 0:
                    tom.append(x)
                    if len(tom) >= n:
                        break
        return tom[n-1]