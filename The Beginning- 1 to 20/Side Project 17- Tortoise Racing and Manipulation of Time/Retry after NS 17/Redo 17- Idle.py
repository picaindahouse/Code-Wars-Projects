def race(v1, v2, g):
    if v1 > v2:
        return None 
    import datetime
    t_seconds = int((g/(v2 - v1)) * 60 * 60)
    tom = datetime.datetime(1,1,1) + datetime.timedelta(seconds = t_seconds)
    return [tom.hour, tom.minute, tom.second]   