def second_index(text, some_str):
    first_occurance = text.find(some_str)
    if first_occurance == -1:
        return None
    second_occurance = text.find(some_str, first_occurance + 1)
    if second_occurance == -1:
        return None
    else:
        return second_occurance


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('OK')