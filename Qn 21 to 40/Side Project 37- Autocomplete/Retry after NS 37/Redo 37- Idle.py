def autocomplete(some, dictionary):
    Input = ''.join([x for x in some if x.lower() in 'abcdefghijklmnopqrstuvwxyz'])
    return [x for x in dictionary if (x.lower())[0:len(Input)]==(Input.lower())][:5]