def smth (tom):
    tum , tim , count = [],[],0
    for x in tom:
        if x == '(':
            count += 1
        elif x == ')':
            count -= 1
            if count == 0:
                if tim.count('(') >0:
                    tim = smth(tim)
                    tim.reverse()
                    tim = ['(' if x == ')'else ')' if x == '(' else x for x in tim]
                else:
                    tim.reverse()
                tum.append('(')
                [tum.append(y) for y in tim]
                tum.append(')')
                tim = []
        if count > 0:
            if count == 1:
                if x not in '(':
                    tim.append(x)
            else:
                tim.append(x)
        else:
            if x not in ')':
                tum.append(x)
    return tum
def reverse_in_parentheses(string):
    tom = smth(string)
    return ''.join(tom)