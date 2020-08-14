def multiply (n, size):
    return [n*x for x in range(1,size+1)] 
def multiplication_table(size):
    return [multiply(x,size) for x in range(1,size+1)]


