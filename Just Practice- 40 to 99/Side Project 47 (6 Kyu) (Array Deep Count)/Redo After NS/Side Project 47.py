def deepCount (tom):
    if list in [type(x) for x in tom]:
        return sum([deepCount(x) for x in tom if type(x) == list]) + len(tom)
    else:
        return len(tom)