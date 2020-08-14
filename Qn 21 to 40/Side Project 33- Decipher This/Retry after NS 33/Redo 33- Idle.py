def decipher (text):
    n = len([x for x in text if x.isdigit()])
    return chr(int(text[0:n])) + text[n:] if len(text) <= (n + 1) else chr(int(text[0:n])) + text[-1] + text[n+1:-1] + text[n]
def decipher_this(string):
    return string if not string else ' '.join([decipher(x) for x in string.split()])