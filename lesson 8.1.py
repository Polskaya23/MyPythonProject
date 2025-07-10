def add_one(some_list:list):
    num_string = ""
    for item in some_list:
        num_string = num_string + str(item)
    # print(num_string)
    num_plus_one = int(num_string) + 1
    # print(num_plus_one)
    digits = [int(x) for x in str(num_plus_one)]
    return digits




assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")