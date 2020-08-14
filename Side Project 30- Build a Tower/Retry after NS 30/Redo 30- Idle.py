def floor (floor_number, n_floors):
    return ' ' * (n_floors - floor_number) + '*' * (floor_number * 2 - 1)  + ' ' * (n_floors - floor_number)
def tower_builder(n_floors):
    return [floor(x, n_floors) for x in range(1,n_floors + 1)]