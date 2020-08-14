def string_letter_count(s):
    tum = []
    [tum.append([str(s.lower().count(x)),x]) if [str(s.lower().count(x)),x] not in tum else 2 for x in s.lower() if x in 'abcdefghijklmnopqrstuvwxyz']
    return ''.join(''.join(x) for x in sorted(tum, key = lambda t: t[1]))