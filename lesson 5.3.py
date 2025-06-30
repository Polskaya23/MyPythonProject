
import string

user_input = input()

user_input = user_input.title().replace(' ', '')

for x in string.punctuation:
    user_input = user_input.replace(x, '')

user_input = '#' + user_input[:140]
print(user_input)

