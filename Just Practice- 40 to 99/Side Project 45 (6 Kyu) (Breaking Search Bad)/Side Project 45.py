def chosen (tom, term):
    return tom if term.lower() in tom.lower() else '1'
def search(titles, term): 
    return [y for y in [chosen(x,term) for x in titles] if y != '1']