def fizz_buzz_custom(string_one = 'Fizz',string_two='Buzz', num_one=3, num_two=5):
    tom = [string_one + string_two if x%num_one==0 and x%num_two == 0 else x for x in range(1,101)]
    tum = [string_one if type(x) == int and x%num_one==0 else x for x in tom]
    return [string_two if type(x) == int and x%num_two==0 else x for x in tum]