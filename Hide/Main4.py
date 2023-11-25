import re

def replace_words_with_dash(input_string):
    pattern = re.compile(r'\b\w+\b')
    result_string = pattern.sub('-', input_string)
    return result_string

input_text = "Hello, my name is: (Jason)"
result = replace_words_with_dash(input_text)
print(result)
