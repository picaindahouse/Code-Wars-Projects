def is_isogram(string):
    return False if len([x for x in [(string.upper()).count(x) for x in string.upper()] if x > 1]) > 0 else True
