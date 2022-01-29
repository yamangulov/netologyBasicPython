from exchange import Rate

def max_course_currency():
    r = Rate().exchange_rates()
    max_value = max({key:value['Value'] for (key,value) in r.items()}.values())
    return [value['Name'] for (key, value) in r.items() if value['Value'] == max_value][0]

print(max_course_currency())