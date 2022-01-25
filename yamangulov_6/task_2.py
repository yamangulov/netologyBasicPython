from datetime import datetime

stream = ['2018-04-02', '2018-02-29', '2018-19-02']

def check_date(date, format):
        try:
            datetime.strptime(date, format)
            return True
        except ValueError:
            return False

for date in stream:
    print(check_date(date,'%Y-%m-%d'))
