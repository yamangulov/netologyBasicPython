import re

emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']

def emails_distribution(emails):
    distribution = {}
    for email in emails:
        pattern = r'\w+@(\w+\.\w+)'
        key = re.match(pattern, email).group(1)
        if key in distribution.keys():
            distribution[key] += 1
        else:
            distribution[key] = 1
    res = ''
    for item in distribution.items():
        res += item[0] + ':' + str(item[1]) + ' '
    return res.strip()

print(emails_distribution(emails))
