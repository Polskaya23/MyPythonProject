import string

def is_palindrome(text:str):
    text_no_punc = ""
    for char in text:
        if char not in string.punctuation:
            text_no_punc += char
    text_no_punc = text_no_punc.lower()
    text_no_punc = text_no_punc.replace(" ", "")
    text_rev = ""
    for char in reversed(text_no_punc):
        text_rev += char
    return text_rev == text_no_punc


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")