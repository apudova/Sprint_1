times = '1h 45m,360s,25m,30m 120s,2h 60s'
times_split = times.split(',')
print(times_split)
# переменная для хранения общей суммы минут
total_minutes = 0

# цикл по отдельным временным значениям
for time in times_split:
    parts = time.split(' ')

    # вложенный цикл по каждому промежутку
    for part in parts:
        if 'h' in part:
            hours = int(part.replace('h', ''))
            total_minutes += hours * 60

        elif 'm' in part:
            minutes = int(part.replace('m', ''))
            total_minutes += minutes

        elif 's' in part:
            seconds = int(part.replace('s', ''))
            total_minutes += seconds / 60

# общая сумма минут составляет
print(total_minutes)