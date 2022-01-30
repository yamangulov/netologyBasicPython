import re

def get_acronym(some_words):
    word_list = re.findall(r'(\w+)', some_words)
    res = ''
    for word in word_list:
        res += word[0]
    return res.upper()

print(get_acronym('Информационные технологии'))
print(get_acronym('Near Field Communication'))