import re

input_text = input('Enter text:')
input_pattern = input('Enter searching word:')


def search_word(text, word):
    count_word = len(re.findall(word, text))
    output_text = re.sub(word, word.capitalize(), text)
    return f'Text include word - {word}:\n{count_word} times.\nReplaced text:\n{output_text}'


print(search_word(input_text, input_pattern))
