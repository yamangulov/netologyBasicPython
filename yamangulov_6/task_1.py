from datetime import datetime

moscow_times_dt = datetime.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y')
print(moscow_times_dt)
print(moscow_times_dt.weekday())

guardian_dt = datetime.strptime('Friday, 11.10.13', '%A, %d.%m.%y')
print(guardian_dt)
print(guardian_dt.weekday())

daily_news_dt =datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')
print(daily_news_dt)
print(daily_news_dt.weekday())


