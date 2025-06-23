num1 =float(input())
operation = input()
num2 = float(input())
if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)
elif operation == '/':
    if num2 ==0:
        print("Error: division by zero is not possible")
    else:
        result = num1 / num2
        print(result)
else:
    print("Error: invalid operation")



