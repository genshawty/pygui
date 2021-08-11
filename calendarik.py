import calendar
from datetime import datetime

days = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}
months = {1: 'Января', 2: 'Февраля', 3: 'Марта', 4: 'Апреля', 5: 'Мая', 6: 'Июня', 7: 'Июля', 8: 'Августа', 9: 'Сентября', 10: 'Октября', 11: 'Ноября', 12: 'Декабря'}

curr_datetime = datetime.now()

year, month, day =  curr_datetime.year, curr_datetime.month, curr_datetime.day

max_days = calendar.monthrange(year, month)[1]

a = 0

for _ in range(10):
    if day > max_days:
        day = 1
        if month == 12:
            month = 1
            max_days = calendar.monthrange(year, month)[1]
            year += 1
        else:
            month += 1

    name_day = days[calendar.weekday(year, month, day)]

    print(f'{name_day}, {day} {months[month]}')

    day += 1