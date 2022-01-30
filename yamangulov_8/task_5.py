import re

some_text = 'Эталонной реализацией Python является интерпретатор CPython, поддерживающий большинство активно используемых платформ. Он распространяется под свободной лицензией Python Software Foundation License, позволяющей использовать его без ограничений в любых приложениях, включая проприетарные.'

rus_vowels = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
eng_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
vowels = rus_vowels + eng_vowels

def get_letter_types(text):
    word_list = re.findall(r'(\w+)', text)
    res = {'Слов на гласные буквы: ': 0, 'Слов на coгласные буквы: ': 0}
    for word in word_list:
        if word[0].lower() in vowels:
            res['Слов на гласные буквы: '] += 1
        else:
            res['Слов на coгласные буквы: '] += 1
    string_res = ''
    for item in res.items():
        string_res += item[0] + str(item[1]) + ' '
    return string_res.strip()

print(get_letter_types(some_text))