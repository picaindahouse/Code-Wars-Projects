tom = str.maketrans('aeiou','12345')
tim = str.maketrans('12345','aeiou')
def encode(st):
    return st.translate(tom)
def decode(st):
    return st.translate(tim)