def namelist(names):
    if names == []:
        return ''
    tom = [names[i]['name'] for i,x in enumerate(names)]
    return '{}{}'.format(''.join([str(x) + ', ' for x in tom][0:-2]) if len(tom) >=3 else '' ,str(tom[-2]) + ' & ' + str(tom[-1]) if len(tom) >= 2 else tom[-1])