lst = [0, 1, 7, 2, 4, 8]
lst_even = lst[::2]
sum_of_even = 0
for x in lst_even:
    sum_of_even = sum_of_even + x
if sum_of_even == 0:
    final_result = 0
else:
    final_result = sum_of_even * lst[-1]
print(final_result)