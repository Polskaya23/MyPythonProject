
user_input = input("Enter an integer: ")
digits_tuple = tuple(user_input)

mult_result = 1
final_result = 10
while final_result > 9:
    # print(digits_tuple)
    for digit in digits_tuple:
        mult_result = mult_result * int(digit)
    final_result = mult_result
    digits_tuple = tuple(str(final_result))
    mult_result = 1

print(final_result)


