import re

data = input('Please, enter your password:')


def password_validator(data):
    pattern_length = r'.{8,50}'
    pattern_upper = r'[A-Z]'
    pattern_lower = r'[a-z]'
    pattern_digit = r'\d'
    pattern_symbol = r'[^\w\s]'
    if not re.findall(pattern_length, data):
        return f'Password must be longer than 8 symbols!'
    if not re.findall(pattern_upper, data):
        return f'Password must has a upper letter!'
    if not re.findall(pattern_lower, data):
        return f'Password must has a lower letter!'
    if not re.findall(pattern_digit, data):
        return f'Password must has a digit!'
    if not re.findall(pattern_symbol, data):
        return f'Password must has a symbol!'
    return f'Your password - {data}!'


print(password_validator(data))
