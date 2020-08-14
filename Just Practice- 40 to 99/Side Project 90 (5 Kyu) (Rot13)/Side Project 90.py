def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' * 2
    return ''.join([x for x in [alphabet[alphabet.index(x) + 13] if x in alphabet else alphabet[alphabet.index(x.lower()) + 13].upper() if x.lower() in alphabet else x if x.lower() not in alphabet else None for x in message] if x != None])