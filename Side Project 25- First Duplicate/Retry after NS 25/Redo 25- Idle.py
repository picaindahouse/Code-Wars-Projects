def first_dup(s):
    return None if not [x for x in s if s.count(x) > 1] else [x for x in s if s.count(x) > 1][0]