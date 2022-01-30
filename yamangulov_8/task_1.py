import re

def validate_car_id(car_id):
    pattern = r'([АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2})(\d{2,3})'
    res = re.match(pattern, car_id)
    if res:
        print('Результат: Номер ' + res.group(1) + ' валиден. Регион: ' + res.group(2))
    else:
        print('Результат: Номер не валиден')

validate_car_id('А222ВС96')
validate_car_id('АБ22ВВ193')