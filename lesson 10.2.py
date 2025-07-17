def first_word(sentence: str):
    pos = 0
    word_start_pos = -1
    word_end_pos = -1
    while pos < len(sentence):
        if word_start_pos == -1:
            if sentence[pos].isalpha() or sentence[pos] == "'":
                word_start_pos = pos
        else:
            if sentence[pos] in [' ', '.', ',']:
                word_end_pos = pos
            elif pos == len(sentence) - 1 and (sentence[pos].isalpha() or sentence[pos] == "'"):
                word_end_pos = pos + 1
        if word_start_pos != -1 and word_end_pos != -1:
            return sentence[word_start_pos:word_end_pos]
        pos += 1


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
