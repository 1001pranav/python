def capitalize_word(string: str):
    return string.capitalize()

def reverse_string(string: str):
    return "".join(reversed(string))

def word_count(string: str):
    words_list = string.split(" ")
    return len(words_list)