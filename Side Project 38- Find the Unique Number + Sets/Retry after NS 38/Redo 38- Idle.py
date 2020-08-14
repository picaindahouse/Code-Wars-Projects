def find_uniq(arr):   
    tom = sorted(arr)
    if tom[0] != tom[1]:
        if tom[0] != tom[-1]:
            return tom[0]
    else:
        return tom[-1]