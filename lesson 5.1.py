import string
import keyword

user_input = input()

result = True

if user_input[0].isdigit():
    result = False

for x in user_input:
    if x.isupper() or x == ' ':
        result = False
        break

if keyword.iskeyword(user_input):
    result = False

if  user_input.count('_') > 1:
    result = False

punctuation_except_underscore = string.punctuation.replace('_', '')

has_other_punctuation = any(char in punctuation_except_underscore for char in user_input)

if (has_other_punctuation):
    result = False


print(result)

