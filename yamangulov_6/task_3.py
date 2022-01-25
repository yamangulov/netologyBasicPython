from datetime import datetime
from datetime import timedelta

def date_range(start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        if start_date > end_date:
            raise ValueError('start_time is more than end_time!')
        date_list = []
        while start_date <= end_date:
            date_list.append(datetime.strftime(start_date, '%Y-%m-%d'))
            start_date = start_date + timedelta(days=1)
        return date_list
    except ValueError:
        return []

print(date_range('2012-01-01', '2011-12-22'))
print(date_range('2012-01-01', '2012-25-22'))
print(date_range('2012-24-01', '2012-01-22'))
print(date_range('2012-01-01', '2012-01-20'))