def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
    begin: first element of sequence
    end: number of elements in sequence
    func: function that generates values for sequence
    """
    count = 1
    return_val = begin
    while count <= end:
        yield return_val
        return_val = func(return_val)
        count += 1

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')