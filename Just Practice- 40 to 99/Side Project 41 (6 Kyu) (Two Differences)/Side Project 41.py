def two_negative (x):
    return x-2
  
def twos_difference(tim):
    return sorted([(two_negative(x),x) for x in tim if two_negative(x) in tim])

