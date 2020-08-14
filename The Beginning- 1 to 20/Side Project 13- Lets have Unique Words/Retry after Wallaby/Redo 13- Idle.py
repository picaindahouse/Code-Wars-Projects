def unique_in_order(tom):
    tim = []
    [tim.append(x) for x in tom if tim == [] or x != tim[-1]]
    return tim