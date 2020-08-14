def letter_count(s):
    return {x:s.count(x) for x in sorted(s)}