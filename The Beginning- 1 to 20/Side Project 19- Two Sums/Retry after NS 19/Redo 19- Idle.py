def two_sum (tom, n):
    return [[i,j] for i,x in enumerate(tom) for j,y in enumerate(tom) if x + y == n and i != j][0]