def find_unique_value(some_numbers: list):
    for num in some_numbers:
        if some_numbers.count(num) == 1:
            return num
    return None

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# У домашньому завданні не було вказано, яким має бути повернене значення,
# якщо у списку немає унікального числа.
# Тому я додала код для обробки цієї ситуації, тому що воно підкреслювало лінію 2
assert find_unique_value([1, 1, 1, 1]) is None, 'Test4'

print("OK")

