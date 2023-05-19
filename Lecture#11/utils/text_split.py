from flask import request, abort


def input_text_lines(text):
    try:
        num_parts = int(request.form['num_lines'])

        words = text.split()

        num_words = len(words)
        print(num_words)
        words_per_part = num_words // num_parts
        words_remainder = num_words % num_parts

        part_word_counts = [words_per_part] * num_parts
        for i in range(words_remainder):
            part_word_counts[i] += 1

        start = 0
        parts = []
        for i in range(num_parts):
            end = start + part_word_counts[i]
            parts.append(" ".join(words[start:end]) + "\n")
            start = end

        text = "".join(parts)
        return f'{text}'
    except:
        return abort(400, 'Please, write number of lines on the pictures.')
