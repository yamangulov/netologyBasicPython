import re

some_string = 'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений.'

def replace_doubles(some_string):
    pattern = r'(\w+)(\s+\1)+'
    return re.sub(pattern, r'\1', some_string)

print(replace_doubles(some_string))