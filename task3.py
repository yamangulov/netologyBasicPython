import datetime

day=int(input("Введите день:"))
month=int(input("Введите месяц:"))

if month > 12:
    print("Месяц должен быть от 1 до 12")
    exit()
elif ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12)
    and (day > 31)):
    print("В этом месяце не может быть больше 31 дня")
    exit()
elif (month == 2 and day > 29 ):
    print("В феврале не может быть больше 29 дней")
    exit()
else:
    print("В этом месяце не может быть больше 30 дней")
    exit()

year=datetime.datetime.now().year
date=datetime.datetime(year, month, day)

if datetime.datetime(year, 3, 21) <= date <= datetime.datetime(year, 4, 20):
    print("Ваш знак зодиака: Овен")
elif datetime.datetime(year, 4, 21) <= date <= datetime.datetime(year, 5, 21):
    print("Ваша знак зодиака: Телец")
elif datetime.datetime(year, 5, 22) <= date <= datetime.datetime(year, 6, 21):
    print("Ваш знак зодиака: Близнецы")
elif datetime.datetime(year, 6, 22) <= date <= datetime.datetime(year, 7, 22):
    print("Ваш знак зодиака: Рак")
elif datetime.datetime(year, 7, 23) <= date <= datetime.datetime(year, 8, 21):
    print("Ваш знак зодиака: Рак")
elif datetime.datetime(year, 8, 22) <= date <= datetime.datetime(year, 9, 23):
    print("Ваш знак зодиака: Дева")
elif datetime.datetime(year, 9, 24) <= date <= datetime.datetime(year, 10, 23):
    print("Ваш знак зодиака: Весы")
elif datetime.datetime(year, 10, 24) <= date <= datetime.datetime(year, 11, 22):
    print("Ваш знак зодиака: Скорпион")
elif datetime.datetime(year, 11, 23) <= date <= datetime.datetime(year, 12, 22):
    print("Ваш знак зодиака: Стрелец")
elif datetime.datetime(year, 12, 23) <= date <= datetime.datetime(year + 1, 1, 20):
    print("Ваш знак зодиака: Козерог")
elif datetime.datetime(year, 1, 21) <= date <= datetime.datetime(year, 2, 19):
    print("Ваш знак зодиака: Водолей")
else:
    print("Ваш знак зодиака: Рыбы")