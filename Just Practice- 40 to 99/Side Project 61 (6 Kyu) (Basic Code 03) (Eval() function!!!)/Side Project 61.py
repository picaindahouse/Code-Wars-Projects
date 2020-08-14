def calculate_string(st): 
    return str(round(eval(''.join([x for x in st if x.isdigit() or x in '.+-*/']))))