import re

pattern = r'((\+{0,1}7)|8)((\s\d{3}\s)|(\(\d{3}\)))\s{0,1}\d{3}[-\s]\d{2}[-\s]\d{2}'

def phone_validate(phone):
    res = re.match(pattern, phone)
    if res:
        return res.group()
    else:
        return 'Номер не валиден'

print(phone_validate('+7 955 555-55-55'))
print(phone_validate('8(955)555-55-55'))
print(phone_validate('+7 955 555 55 55'))
print(phone_validate('7(955) 555-55-55'))
print(phone_validate('423-555-55-5555'))
print(phone_validate('123-456-789'))