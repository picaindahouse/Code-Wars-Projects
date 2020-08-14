def split (tom):
    if len(tom)%2 == 0:
        return [x + y for i,x in enumerate(tom[0:int(len(tom)/2)]) for r,y in enumerate(tom[int(len(tom)/2):]) if i == r]
    else:
        tim = list(enumerate(tom[0:int(len(tom)/2)]))
        tim.insert(0,(-1,0))
        return[x + y for i,x in tim for r,y in enumerate(tom[int(len(tom)/2):]) if r == i + 1]


def split_and_add(numbers, n):
    tries = 0
    while tries != n and len(numbers) != 1:
        tries += 1
        numbers = split(numbers)
    return numbers

