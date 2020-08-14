def encrypt (text):
    return str(ord(text[0])) + text[1:] if len(text) <= 2 else str(ord(text[0])) + text[-1] + text[2:-1] + text[1]
def encrypt_this(word):
        return word if not word else ' '.join([encrypt(x) for x in word.split()])