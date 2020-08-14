def delete_nth(order,max_e):
    tim = []
    [tim.append(x) for x in order if tim.count(x) < max_e]
    return tim